#libraries
import os
import json
import time
import logging
import uvicorn
import traceback
import numpy as np
import pandas as pd
from rockset import ParamDict
from datetime import datetime
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from rockset.exception import LimitReached
from typing import Any, Dict, List, Optional
from fastapi.middleware.cors import CORSMiddleware
from rockset import Client, Q, F, P, ParamDict , InputError
from fastapi import Body, FastAPI, File, Form, Request

app = FastAPI(debug=True)


#adding CORS(for allowing to hit from different addresses)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def retry(ExceptionToCheck, tries=4, delay=1, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        # @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            result=[]
            while mtries > 1:
                try:
                    result = f(*args, **kwargs)
                    return result
                except ExceptionToCheck as e:
                    print("exception: ", e)
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            try:
                result = f(*args, **kwargs)
            except:
                result=[]
            return result

        return f_retry  # true decorator

    return deco_retry


def UpdatAdObj(channel_name,adBreaksStart,adBreakEnd):
    '''
    Creates and Object of class adObject and assigns values to required attributes

    arguments:
        channel_name: name of the channel (eg: MTVC or FXX)
        adBreaksStart: start time of the fps (adbreak) (eg: )
        adBreakEnd: end time of the fps (adbreak) (eg:)
   
    returns: adObj (adObject with required attributes)
    '''
    adObj = adObject()
    adObj.rockset_api_key = "WqMRoAPCvuvVvZUEcFhtdacVU9jqHPufgFbPdGIsjCuW8GPLqKluoMLN2lEG53XV"
    adObj.rockset_api_key_backlog= "WqMRoAPCvuvVvZUEcFhtdacVU9jqHPufgFbPdGIsjCuW8GPLqKluoMLN2lEG53XV"
    adObj.network_id = channel_name
    # adObj.client =
    adObj.backlog_client = Client(api_key = 'WqMRoAPCvuvVvZUEcFhtdacVU9jqHPufgFbPdGIsjCuW8GPLqKluoMLN2lEG53XV')
    adObj.client = Client(api_key ='WqMRoAPCvuvVvZUEcFhtdacVU9jqHPufgFbPdGIsjCuW8GPLqKluoMLN2lEG53XV')
    adObj.channel_name = channel_name
    # adObj.date = date
    adObj.adBreaksStart = adBreaksStart
    adObj.adBreakEnd = adBreakEnd
    return adObj



#                       Helper Functions


# Defining the adObject class for adObj variables
class adObject:
    '''
    Used to access variables ( carry around variables )
   
    '''
    client =None

    backlog_client=None
    capture_root_path=None
    audio_stage1_qlambda = 'direct_stage1'
    audio_stage1_tag = 'development' #'prod'
    #large lambda
    large_stage1_qlambda = 'direct_test1'
    large_stage1_tag = 'development' #'prod'
    #audio verify lambda
    audio_verify_qlambda = 'direct_audio_verify'
    audio_verify_tag = 'development'

    schedules__path = 'admon/schedule'
    audio_fps_path =  'admon/AUDIO_FEAT'
    stage1_filtered_result = None
    longInterval = 30000
    largeInterval = 30000
    ads_collection_name = 'ads_daily-superset'


    #ad databse search related  alias
    ads_alias_key ='current_ad_audios_alias'
    ads_alias_value ='ads_daily-superset'
    #large_masters_ads
    large_audios_alias_key ='large_ad_audios_alias'
    large_audios_alias_value ='large_masters_ad_test'
   
    ad_break_list=None
    date=None
    network_id=None
    verified_result=None

    start_hour = 0
    end_hour = 2400



# Function to calculate the end hour
def calculate_end_hour(start_hour, duration):
    '''
    calculate_end_hour()  : to get the end_time in required military format using input start_hour
    start_hour         : Should be in 4 digits millitary time
                        eg. 0000,0045,1215,1300,2345
                        1 Hour is divided in 4 halves.
                        Collection_name should be
                        HHMM where :
                        MM -> 00,15,30,45
    duration: duration to add in minutes to start_hour (eg: 15)
   
    returns: end_time (duration added to start_hour)
    '''

    hours = int(start_hour[0:2])
    mins = int(start_hour[2:])
    mins = mins + int(duration)

    if mins >= 60 :
        hours = hours + 1
        mins = mins%60      

    if hours < 10 :
        end_time = '0'+ str(hours)
    else :
        end_time = str(hours)
 
    if mins < 10 :
        end_time = end_time + '0' + str(mins)
    else :
        end_time = end_time + str(mins)


    return end_time


# Function for Stage1 ad search filter
@retry(Exception, tries=4,delay = 1 , backoff = 1)
def ads_stage1_search_filter( adObj, start_timestamp , end_timestamp  , fps ,debug=True ):
    '''
    Performs Stage1 Search and filter
    excutes audio_stage1_qlambda(direct_stage1) if duration is less than 10 mins  ,
    if > 10 mins  large_stage1_qlambda(direct_test1) is used

    arguments:
            adObj : ad-detect object with attributes assigned to it .
            start_timestamp: start timestamp of the query (start timestamp of fps)(in Unix format)(Eg: 1630146970)
            end_timestamp: end timestamp of the query (end timestamp of fps)(in Unix format) (Eg:  1630147076)
            fps: fingerprints (List of dicts Eg: [{"timestamps":11100,"fingerprints":"0x198c","id":"FXX"},{"timestamps":30700,"fingerprints":"0x19e7","id":"FXX"},...] )
            debug: if True extra statements will be printed

    returns: sel_df ( list of filtered matches )
    '''
    rs = adObj.client
    # print(rs)
    qlambda = rs.QueryLambda.retrieveByTag(
    #qlambda = rs.QueryLambda.retrieve(
        adObj.audio_stage1_qlambda ,
        tag = adObj.audio_stage1_tag ,
        #version= adObj.audio_stage1_version ,
        workspace='commons')

    #do long seaches only on backlog orgs
    backlog_rs = adObj.backlog_client
    qlambdaL = backlog_rs.QueryLambda.retrieveByTag(
        adObj.large_stage1_qlambda,
        tag = adObj.large_stage1_tag ,
        #version= adObj.audio_stage1_version ,
        workspace='commons')

    '''
    Final ad break list extracted from logo bounds.
    '''
    ad_break_list = [(start_timestamp,end_timestamp)]
    df_list = []
    sel_df = []
    df_list_l = []
    sel_df_l = []

    '''
    Create name of the audio stage1 collection e.g. AudioStage1_20210204.
    If that collection is not present. Create it.
    '''
    #collection_name_audio_stage1 = 'AudioStage1_' + collection_name    
    #create_db( adObj, adObj.client, collection_name_audio_stage1 )

    '''
    For each start and max time from ad breaks,
    Run the queries and upload the results on rockset.
    '''
    audio_stage1_start = time.time()
    print("AdBreak list: {}".format(ad_break_list))
    for start_time, max_time in ad_break_list:
        start_time = int(start_time)
        max_time = int(max_time)
        query_id = adObj.network_id

        overlap = 5000
        params = ParamDict()
        paramsl = ParamDict()
        #print ("start_time params1 {}".format(paramsl) )
        #enable large masters search for informaercials
        enable_large_stage1 = 0
        params['interval'] = 10000 # to avoid exception because of 100MB mem
        #paramsl['interval'] = 7000
        #get InfoCommercial timings
       
        #server_name = get_servername(channel_name)
        #schedule_root_path = os.path.join(adObj.capture_root_path , server_name , adObj.schedules__path , adObj.network_id , adObj.date )
        #t_list = GetInfoComercialTimings(channel_name = adObj.network_id , date = adObj.date , schedule_root_path = schedule_root_path )
        #check if the current interval is in info commercial time
        #if  any([int(x[0])<=int(adObj.start_hour)<int(x[1]) for x in t_list]) and  any([int(x[0])<=int(adObj.end_hour)<int(x[1]) for x in t_list]):
        #    enable_large_stage1 = 1
        #    print("In InfoCommercial timings , starting large ads search")
        #else:
        #    print("Not in InfoCommercial timings ")


        if max_time - start_time > 600000:
            paramsl['overlap'] = adObj.longInterval
            params['interval'] = adObj.longInterval
            # disabled large search
            enable_large_stage1 = 1
        params['object_id'] = query_id
        params['start_time'] =  start_time
        paramsl['object_id'] = query_id
        #print( 'Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
        #print("params stage1 {}".format(params) )
        #print("stage1 search start {}  and end: {}".format(start_time,max_time))
        #print("lambda used is:{} and version is {}".format(adObj.audio_stage1_qlambda,adObj.audio_stage1_version))


        while params['start_time'] < max_time :
            result = []
            #direct stage1
            get_start_time = params['start_time']
            get_end_time = params['start_time'] + params['interval']
            # fps_folder = os.path.join(adObj.capture_root_path , server_name , adObj.audio_fps_path , adObj.network_id , adObj.date )
            # params['qintArray'] = json.dumps(GetRqdFps( start_time = get_start_time ,end_time = get_end_time , input_folder = fps_folder ))
            params["qintArray"] = json.dumps(fps)
            if debug:
                print("parameters for lambda: {} are: {}".format(adObj.audio_stage1_qlambda,params))
            try :
                result = qlambda.execute(parameters=params).results

            except LimitReached:
                print("Query storage limit reached for  stage1 Q retrying with 8500 interval ")
                params['interval'] = 8500
                print("parameters for lambda are: {}".format(params))
                try :
                    result = qlambda.execute(parameters=params).results
                except LimitReached:
                    time.sleep(0.3)
                    print("Query storage limit reached for  stage1 Q retrying with 7500 interval ")
                    params['interval'] = 7500
                    try:
                        result = qlambda.execute(parameters=params).results
                    except LimitReached:
                        time.sleep(0.3)
                        #print("Query storage limit reached  7500 interval , skipping the search")
                        pass
                        print("Query storage limit reached for  stage1 Q retrying with 5000 interval ")
                        params['interval'] = 5000
                        try:
                            result = qlambda.execute(parameters=params).results
                        except LimitReached:
                            time.sleep(0.3)
                            print("Query storage limit reached  5000 interval , skipping the search")
                            pass
                #pass

            if params['start_time'] % 500000 == 0:
                pass
                # print( '{} - start time - {}' .format(query_id, params['start_time'] ) )

            params['start_time'] = params['start_time'] + overlap
            #paramsl['start_time'] = params['start_time'] + overlap
            #print('Stage1 result -> {}'.format(result))
            try:
                if len(result) > 0:
                    for row in result:
                        if 'ref_duration' in row:
                            df_list.append( {'qid':row['qid'], 'rid':row['rid'], 'cnt':row['cnt'] , 'offset_bin':row['offset_bin'],
                                'q_start':row['q_start'], 'q_end':row['q_end'], 'ref_duration':row['ref_duration'] } )
                        else:
                            df_list.append( {'qid':row['qid'], 'rid':row['rid'], 'cnt':row['cnt'] , 'offset_bin':row['offset_bin'],
                                 'q_start':row['q_start'], 'q_end':row['q_end'] } )
            except:
                print( 'Exception at stage1 df_list : Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
                traceback.print_exc()

        # if debug:
        #     print("stage search results for {} at {} before filtering (df_list) : {}".format( start_time, query_id, df_list ) )

        #Filter now
        try:
            for r in df_list:
                #if row['rid'] == 110442446:
                #    print('row in id acc: {}'.format(row))
                #ignore if offset_bin is near 0; or already in list
                if r['rid'] not in list(set([x['rid']  for x in sel_df ] )):
                    r['minq'] = r['q_start']
                    r['maxq'] = r['q_end']
                    #print('1. add r: {}'.format(r))
                    sel_df.append(r)
                elif r['rid'] in list(set([x['rid']  for x in sel_df ] )):
                    pos_locs = [x['rid'] for x in sel_df]
                    skip = 0
                    for pos in range(0, len(pos_locs)):
                        max_bin_delta = 1 + int(abs(r['q_start'] -sel_df[pos]['q_start'])/20000)
                        if sel_df[pos]['rid'] == r['rid'] and abs(r['offset_bin'] - sel_df[pos]['offset_bin'] ) <= max_bin_delta:
                            skip = 1
                    if skip == 0:
                        r['minq'] = r['q_start']
                        r['maxq'] = r['q_end']
                        #print('2. add r: {}'.format(r))
                        sel_df.append(r)
                        #elif r['cnt'] > [x['cnt'] for x in sel_df if x['rid'] == r['rid']][0] :
                    elif sel_df[pos]['rid'] == r['rid'] and r['cnt'] > sel_df[pos]['cnt'] and abs(r['offset_bin'] - sel_df[pos]['offset_bin'] ) <= max_bin_delta:
                        #replace previous match
                        r['minq'] = r['q_start']
                        r['maxq'] = r['q_end']
                        #print('3. update r: {}'.format(r))
                        sel_df[pos] = r
            #print("sel_df ids: {}".format(sel_df))        
        except:
            # print( 'Exception at stage1 sel_df : Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
            traceback.print_exc()

        try:
            for row in sel_df:
                row['mcnt'] = row['cnt']
                row['hits'] = 1
                row['gcnt'] = row['cnt']
                for r in df_list:
                    query_duration = abs(row['q_start'] - r['q_start'])
                    if r['rid'] == row['rid'] and row['q_start'] != r['q_start'] and abs(r['offset_bin'] - row['offset_bin']) <= 1 + int(query_duration/20000):
                        row['gcnt'] += r['cnt']
                        row['hits'] +=1
                        if row['mcnt'] < r['cnt']:
                             row['mcnt'] = r['cnt']
                        if row['maxq'] < r['q_end']:
                             row['maxq'] = r['q_end']
                        if row['minq'] > r['q_start']:
                             row['minq'] = r['q_start']
            if debug:
                print ('sel_df after filtering: {}'.format(sel_df))
        except:
            # print( 'Exception at stage1 sel_df filter : Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
            traceback.print_exc()
         #enable large masters search
        #paramsl=params.copy()
        #paramsl['start_time'] =  start_time
        if  enable_large_stage1 == 1:
            overlap = adObj.longInterval
            paramsl['overlap'] = adObj.longInterval
            params['interval'] = adObj.longInterval
            params['start_time'] =  int(start_time)
        #print ("start_time params1 {} , max_time {}".format(params1, max_time) )
        while  params['start_time'] < max_time and enable_large_stage1 == 1:
            print( 'Start Time of Large Stage1 query : {}, Max Time of Stage1 query {}'.format(params['start_time'], max_time))

            result = []
            get_start_time = params['start_time']
            get_end_time = params['start_time'] + adObj.largeInterval
            print("get_start_time ,get_end_time", get_start_time ,get_end_time)
            # fps_folder = os.path.join(adObj.capture_root_path , server_name , adObj.audio_fps_path , adObj.network_id , adObj.date )
            # params['qintArray'] = json.dumps(GetRqdFps( start_time = get_start_time ,end_time = get_end_time , input_folder = fps_folder ))
            params['interval'] = adObj.largeInterval
            params["qintArray"] = json.dumps(fps)

            try :
                result = qlambdaL.execute(parameters=params).results
            except:
                # print( 'Exception at stage1 Q : Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
                traceback.print_exc()

            if params['start_time'] % 500000 == 0:
                pass
                # print( '{} - start time - {}' .format(query_id, params['start_time'] ) )

            params['start_time'] = params['start_time'] + overlap

            if debug:
                print('Large Stage1 result -> {}'.format(result))
            try:
                if len(result) > 0:
                    for row in result:
                        if 'ref_duration' in row:
                            df_list_l.append( {'qid':row['qid'], 'rid':row['rid'], 'cnt':row['cnt'] , 'offset_bin':row['offset_bin'],
                                'q_start':row['q_start'], 'q_end':row['q_end'], 'ref_duration':row['ref_duration'] } )
                        else:
                            df_list_l.append( {'qid':row['qid'], 'rid':row['rid'], 'cnt':row['cnt'] , 'offset_bin':row['offset_bin'],
                                 'q_start':row['q_start'], 'q_end':row['q_end'] } )
            except:
                #print( 'Exception at stage1 large df_list_l : Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
                traceback.print_exc()

        #Filter now
        try:
            for r in df_list_l:
                #if row['rid'] == 110442446:
                #    print('row in id acc: {}'.format(row))
                #ignore if offset_bin is near 0; or already in list
                if r['rid'] not in list(set([x['rid']  for x in sel_df_l ] )):
                    r['minq'] = r['q_start']
                    r['maxq'] = r['q_end']
                    #print('1. add r: {}'.format(r))
                    sel_df_l.append(r)
                elif r['rid'] in list(set([x['rid']  for x in sel_df_l ] )):
                    pos_locs = [x['rid'] for x in sel_df_l]
                    skip = 0
                    for pos in range(0, len(pos_locs)):
                        max_bin_delta = 1 + int(abs(r['q_start'] -sel_df_l[pos]['q_start'])/20000)
                        if sel_df_l[pos]['rid'] == r['rid'] and abs(r['offset_bin'] - sel_df_l[pos]['offset_bin'] ) <= max_bin_delta:
                            skip = 1
                    if skip == 0:
                        r['minq'] = r['q_start']
                        r['maxq'] = r['q_end']
                        #print('2. add r: {}'.format(r))
                        sel_df_l.append(r)

                    elif sel_df_l[pos]['rid'] == r['rid'] and r['cnt'] > sel_df_l[pos]['cnt'] and abs(r['offset_bin'] - sel_df_l[pos]['offset_bin'] ) <= max_bin_delta:
                        #replace previous match
                        r['minq'] = r['q_start']
                        r['maxq'] = r['q_end']
                        #print('3. update r: {}'.format(r))
                        sel_df_l[pos] = r
            if debug:
                print("sel_df ids: {}".format(sel_df))
        except:
            #print( 'Exception at large sel_list_l : Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
            traceback.print_exc()

        try:
            multiple_large = 4*float(adObj.largeInterval)/float(adObj.longInterval)
            for row in sel_df_l:
                row['mcnt'] = row['cnt']
                row['hits'] = 1 * multiple_large
                row['gcnt'] = row['cnt'] * multiple_large
                for r in df_list_l:
                    query_duration = abs(row['q_start'] - r['q_start'])
                    if r['rid'] == row['rid'] and row['q_start'] != r['q_start'] and abs(r['offset_bin'] - row['offset_bin']) <= 1 + int(query_duration/20000):
                        row['gcnt'] += r['cnt'] * multiple_large
                        row['hits'] +=1*multiple_large
                        if row['mcnt'] < r['cnt']:
                             row['mcnt'] = r['cnt']
                        if row['maxq'] < r['q_end']:
                             row['maxq'] = r['q_end']
                        if row['minq'] > r['q_start']:
                             row['minq'] = r['q_start']
            if debug:
                print ('sel_df_l after filtering: {}'.format(sel_df_l))
        except:
           # print( 'Exception at large sel_list_l filter : Start Time of {} Stage1 query : {}, Max Time of Stage1 query {}'.format(query_id, start_time, max_time))
            traceback.print_exc()


    audio_stage1_end = time.time()
    print(" --- Time Taken To Execute Audio Stage 1 = {}--- ".format(audio_stage1_end - audio_stage1_start))
    # if debug:
        #print(" --- Results for {} at {}  from audioStage1_and_filter : {}".format(query_id, start_time,sel_df))
    if sel_df_l == None or sel_df_l == []:
        adObj.stage1_filtered_result = sel_df
    else:
        adObj.stage1_filtered_result = sel_df.extend(sel_df_l)
        if debug:
            print ('sel_df after  appending: {}'.format(sel_df))
    #print("stage 1 large search results: {}".format(sel_df_l))
    #adObj.stage1_filtered_result = sexsl_df
    #ret = rs.Collection.add_docs( collection_name_audio_stage1 , df_list )
    return sel_df

# Function to verify ad detects
@retry(Exception, tries=4,delay = 1 , backoff = 1)
def verify_ads_ad_detect(selfdf , adObj , fps , debug = True) :
    '''
    Performs Verification for stage1 results
    excutes audio_verify_qlambda(direct_audio_verify)  and does extra checks for verifying matches

    arguments:
            selfdf : list of stage1 search and filtered matches
            adObj : ad-detect object with attributes assigned to it .
            fps: fingerprints (List of dicts Eg: [{"timestamps":11100,"fingerprints":"0x198c","id":"FXX"},{"timestamps":30700,"fingerprints":"0x19e7","id":"FXX"},...] )
            debug: if True extra statements will be printed

    returns: df_list ( list of verified matches )
    '''
    #debug=1

    if debug:
        print("Inside verify_audio_matches")
    rs = adObj.client
    # #unused lambda
    # qlambda_audio_filter = rs.QueryLambda.retrieve(   #retrieveByTag
    #     adObj.audio_filter_qlambda ,
    #     version=adObj.audio_filter_version ,          #'prod' #audio_filter_tag
    #     workspace='commons')

    qlambda_audio_verify = rs.QueryLambda.retrieveByTag(
    #qlambda_audio_verify = rs.QueryLambda.retrieve(
        adObj.audio_verify_qlambda ,
        tag= adObj.audio_verify_tag ,
        #version= adObj.audio_verify_version ,
        workspace='commons')

    params = ParamDict()
    params2 = ParamDict()

    ad_break_list = adObj.ad_break_list
    df_list = []

    '''
    Create name of the verified stage1 collection e.g. VerifiedAudio_20210204.
    If that collection is not present. Create it.
    '''
    #collection_name_verified = 'VerifiedAudio_' + collection_name
    #create_db( adObj, adObj.client, collection_name_verified )

    '''
    For each start and max time from ad breaks,
    Run the queries and upload the results on rockset.
    '''

    #commenting not required code
    filter_verify_start_time = time.time()
    query_id = adObj.network_id
    params2['object_id'] = str(query_id)
    '''
    for start_time, max_time in ad_break_list :

        start_time = int(start_time)
        max_time = int(max_time)
        query_id = adObj.network_id
        print( 'Start Time of Filter query : {} , Max Time of Filter query {} '.format(start_time, max_time))

        params['qid'] = str(query_id)
        params['interval'] =  20000
        params['q_start'] = start_time
       
        while  params['q_start'] < max_time :
           
            #try:
           
            #    filter_results = qlambda_audio_filter.execute(parameters=params).results

            #except Exception as err:
            #    return err

            if params['q_start'] % 500000 == 0:
                print( ('{} - q_start - {}' ).format(query_id,params['q_start']) )

            params['q_start'] = params['q_start'] + params['interval']
            print("--- Filter Results : {}".format(filter_results) )
    '''
    if not selfdf:
        print("empty stage1 filtered results ")
        return
    else:
        pass
    #print("---- Stage1 filtered results: {}".format(adObj.stage1_filtered_result))
    for res in selfdf:
    #for res in filter_results:
        #print("res in stage1 filtered results: {}".format(res))
        try :
            verify_result = []
            #if its not dict type then discard it
            if not isinstance(res,dict):
                continue
            channel_start = int(res['offset_bin'])*(-1000)
            params2['interval'] = res['ref_duration']
            params2['refid'] = res['rid']
            params2['start_time'] = int(channel_start)
            params2['offset_bin'] = res['offset_bin']
            params2['offset_win'] = 1
            ref_duration=res['ref_duration']

            #if (res['gcnt'] < 11 and res['hits'] == 2):
            #    print("Dropped res['gcnt'] < 11 and res['hits'] == 2 ")
            #    continue
            if (res['gcnt'] < 20 or res['hits'] <= 2 and ref_duration >= 28000):
                if debug:
                    print("Dropped res['gcnt'] < 20 and res['hits'] <= 2 and ref_duration >= 28000" )
                continue
            if (res['gcnt'] < 25 or res['hits'] <= 2 and ref_duration >= 58000):
                if debug:
                    print("Dropped res['gcnt'] < 25 and res['hits'] <= 2  and ref_duration >= 58000" )
                continue
            if (res['gcnt']/(res['ref_duration']/1000) < 0.3) and res['ref_duration'] > 120000 and res['gcnt'] < 100:
            #if (res['gcnt']/(res['ref_duration']/1000) < 0.3) and res['ref_duration'] > 12000 and res['gcnt'] < 100 :
                if debug:
                    print("Dropped res['gcnt']/(res['ref_duration']/1000) < 0.3) and res['ref_duration'] > 120000 and res['gcnt'] < 100" )
                continue
            #add condition to drop weak long matches
            if res['gcnt'] < 40 and res['ref_duration'] > 200000:
                if debug:
                    print("Dropped res > than 200sec and mcnt <40 -> {} , {}, {}".format(res['rid'], res['ref_duration'], res['mcnt']))
                continue
            #to add quick exit for longer matches if mcnt > than 50
            #next add a long match option in parallel / similar code but for informercials
            #print("Input to audio verify qlambda: ",params2)
            if int(res['ref_duration']) > 35000:
                params2['offset_win'] = 2
                if int(res['ref_duration']) > 60000:
                    params2['offset_win'] = int(res['ref_duration']/20000) + 1

            #long match : report to results
            if res['ref_duration'] > 330000 and res['gcnt'] > 180:
                if debug:
                    print ("checking long match : {}".format(res))
                search_interval_ratio = int(adObj.longInterval) / 5000
                res['valid'] = 1
                res['match_secs'] = int(res['hits']) * search_interval_ratio  #number of blocks matching
                res['cnt'] = int(res['gcnt']) * search_interval_ratio #number of blocks matching
                res['qsigs'] = int(res['gcnt'])*1.5
                res['chan_start'] = int(channel_start)
                res['q_start'] = res['minq']
                res['q_end'] = res['maxq']
                res['new_offset'] = res['offset_bin']
                #to add to filter fns
                #min(q_start) as minq, max(q_start) as maxq
                verified_row = res
                if debug:
                    print ("long match detected, move to separate adObj later for long searches; and disbale in current flow: {}".format(res))
                df_list.append( { 'q_start':verified_row['q_start'],'q_end': verified_row['q_end'],'chan_start': verified_row['chan_start'],'new_offset': verified_row['new_offset'],
                                               'cnt': verified_row['cnt'],'rid': verified_row['rid'],'qid': verified_row['qid'],'ref_duration': verified_row['ref_duration'],
                                               'match_secs': verified_row['match_secs'],'qsigs': verified_row['qsigs'], 'valid':verified_row['valid'] } )


                continue
            #try :
            if debug:
                print('params2 for audio verify : {}'.format(params2))
            get_start_time = params2['start_time']
            get_end_time = params2['start_time'] + params2['interval']

            # server_name = get_servername(channel_name)
            # fps_folder = os.path.join(adObj.capture_root_path , server_name , adObj.audio_fps_path , adObj.network_id , adObj.date )
            # params2['qintArray'] = json.dumps(selfdf , adObj , collection_name , debug = True, fps ))
            params2["qintArray"] = json.dumps(fps)
            #print ("params qintArray", params2['qintArray'])
            verify_result = result = qlambda_audio_verify.execute(parameters=params2).results

            #except Exception as err:
            #    traceback.print_exc()

            print("Verified result ->   {}".format(verify_result))

            if len(verify_result):

                for verified_row in verify_result:
                    df_list.append( { 'q_start':verified_row['q_start'],'q_end': verified_row['q_end'],'chan_start': verified_row['chan_start'],'new_offset': verified_row['new_offset'],
                                               'cnt': verified_row['cnt'],'rid': verified_row['rid'],'qid': verified_row['qid'],'ref_duration': verified_row['ref_duration'],
                                               'match_secs': verified_row['match_secs'],'qsigs': verified_row['qsigs'], 'valid':verified_row['valid'] } )
       
        #to retry if there is error due to concurrency from rockset
        except LimitReached:
            raise LimitReached

        except Exception as err :
            print("Exception Occured while getting verified results: {}".format(err))
            #logging.exception("Exception Occured while getting verified results ",exc_info=True)
     
    #adObj.verified_result = df_list
    #print("---- Results from Audio Filter and Audio Verify = {} --- ".format(df_list))
    print("--- Time Taken To execute  Audio Verify = {} --- ".format(time.time() - filter_verify_start_time))
    return df_list

 
def process_time( hours_right_now, minutes_right_now, duration):

    '''
    Converts the time into the format required which is 4 digit millitary.
    Convert into specified intervals,
    15 minutes : 0100-0115, 0115-0130.
    If time right now is 1:25,
    The start and end time returned will be 0100-0115,
    i.e. The previous interval for which the files can be processed.


    Arguments :
            hours_right_now : current hour / hour for which to process ad-detect, (int)
            minutes_right_now : current minute / minute for which to process ad-detect, (int)
            duration : of the interval in minutes.

    Return :
            start and end time converted in millitary format.
    '''

    start_min, end_min = None, None
    end_min = int(minutes_right_now//duration)*duration
    start_min = (end_min - duration)%60

    if end_min == 0 :
        start_hour = (hours_right_now-1)%24
    else :
        start_hour = (hours_right_now)%24
    end_hour = (hours_right_now)%24


    if start_hour < 10 :
        start_time = '0'+str(start_hour)
    else :
        start_time = str(start_hour)

    if end_hour < 10 :
        end_time = '0' + str(end_hour)
    else:
        end_time = str(end_hour)


    if start_min < 10 :
        start_time = start_time + '0' + str(start_min)
    else :
        start_time = start_time + str(start_min)

    if end_min < 10 :
        end_time = end_time + '0' + str(end_min)
    else :
        end_time = end_time + str(end_min)
   
   
    return start_time, end_time

# Function to create a make directory or check if it is existing
def mkdir_or_exist(folder_path):
    '''
    Check if the base directory exists on the server or not.

    input :
            folder_path : path to the base folder.
    returns: folder path
    '''
    if os.path.isdir(folder_path):
        return folder_path

    else:
        os.makedirs(folder_path)


    return folder_path



# Function to save the verified results to the server
def save_to_server(adObj, verified_result):
    '''
    filters the verified results
    arguments:
        adObj: ad object
        verified_result: List of verified results
   
    returns: results_list (list of matches)
   
    '''
    print("Function to save to the server")
    # retrieved_results =  adObj.verified_result
    retrieved_results = verified_result
    results_list = []
    duplicate_rows = {}
    overlap_period = 5000
    mvar=3.0
    qvar=1.8
    lvar=1.0 #1.1 for  17-32 secs; 1.2 for 32-64 s ; 1.27 for 64-128; 1.35 for 128 to 303 ; 1.5 for >303
    #for row in (retrieved_results):
    try:
        for row in sorted(retrieved_results, key= lambda k: k['q_start']) :
            """
            ts = int(row['chan_start'])/1000
            exact_time = (datetime.utcfromtimestamp(ts).strftime('%H%M'))
            if int(exact_time) >= int(adObj.start_hour) and int(exact_time) <= int(adObj.end_hour) :
            """
            ts = int(row['chan_start'])/1000
            ts_end = ts + int(row['ref_duration'])/1000
            exact_time = (datetime.utcfromtimestamp(ts).strftime('%H%M'))
            exact_end = (datetime.utcfromtimestamp(ts_end).strftime('%H%M'))
            if ( int(exact_time) >= int(adObj.start_hour) and int(exact_time) <= int(adObj.end_hour) ) or \
                    (int(exact_end) > int(adObj.start_hour) and int(exact_time) <= int(adObj.end_hour) ):
                results_list.append(row)
                chan_start = row['chan_start']
                cnt = row['cnt']
                ratio = float(int(cnt)/int(row['ref_duration']))*1000
                match_secs = int(row['match_secs'])
                match_ratio = float((match_secs)/(row['ref_duration']/1000.0))
                qsigs = int(row['qsigs'])
                index = len(results_list)-1
                present = 0
                ref_duration = int(row['ref_duration'])

                if (ref_duration > 17000 and ref_duration < 32000):
                    lvar=1.07
                elif (ref_duration  > 32000 and ref_duration  < 64000):
                    lvar=1.14
                elif (ref_duration  > 64000 and ref_duration < 128000):
                    lvar = 1.2
                elif (ref_duration  > 128000 and ref_duration < 305000):
                    lvar = 1.25
                else:
                    lvar = 1.35
                score = lvar * (float(match_secs/float(ref_duration/1000.0)) * mvar + match_ratio \
                                + float(qsigs/float(ref_duration/1000)) * qvar )

                best_score = 0
                for already_present_chan_start in duplicate_rows.keys() :
                    duplicate = 0
                    overlap = None
                    best_score, d_q_start, d_q_end, prev_ratio, prev_match_ratio, prev_match_secs, prev_qsigs, prev_index = duplicate_rows[already_present_chan_start]
                    try:
                        if ref_duration > 33000 and d_q_end -d_q_start > 33000 :
                            overlap_period = 7000
                        elif ref_duration > 33000 and d_q_end -d_q_start > 33000 :
                            overlap_period = 10000
                        elif  ref_duration > 310000 and d_q_end -d_q_start > 310000 :
                            overlap_period = ref_duration / 10
                    except:
                        pass
   
                    if (1) : # ref_duration < 120000 or d_q_end - d_q_start > 120000:  
                        overlap = min(ref_duration+chan_start, int(d_q_end)) - max(chan_start, int(d_q_start))
                        if ref_duration < int(d_q_end) - int(d_q_start):
                            if overlap > 0.4 * ref_duration:
                                duplicate = 1
                        else:
                            if overlap > 0.4 * (int(d_q_end) - int(d_q_start)):
                                duplicate = 1
                    min_start = chan_start
                    max_end = chan_start + ref_duration
                    if ((chan_start >= (already_present_chan_start-overlap_period)) and (chan_start <= (already_present_chan_start + overlap_period)) or duplicate == 1) \
                    or ( (chan_start < (d_q_end-overlap_period) and (chan_start + ref_duration) > (d_q_start + overlap_period) ) ):
                        max_ratio = max(prev_ratio, ratio)
                        max_match_ratio = max(prev_match_ratio * prev_match_secs, match_ratio*match_secs)
                        if score > best_score:
                            best_score = score
                            duplicate_rows[already_present_chan_start] = (score, min_start, max_end, max_ratio, match_ratio, match_secs, qsigs, index)
                            #print("IF. new index, prev_ratio, prev_match_ratio,  prev_match_secs, prev_qsigs", row['rid'], index, prev_ratio, prev_match_ratio,  prev_match_secs, prev_qsigs, prev_index)
                        elif  prev_ratio * prev_match_ratio * prev_match_secs < ratio * match_ratio * match_secs and not (match_secs <= 2 * prev_match_secs or qsigs <= 3 * prev_qsigs ):
                            #print("2. new index, cur prev_ratio, prev_match_ratio,  prev_match_secs, prev_qsigs", row['rid'], index, prev_ratio, prev_match_ratio,  prev_match_secs, prev_qsigs, prev_index)
                            best_score = score
                            duplicate_rows[already_present_chan_start] = (score, min_start, max_end, max_ratio, match_ratio, match_secs, qsigs, index)
                        #else :
                        #    print("Else. prev index, prev prev_ratio, prev_match_ratio,  prev_match_secs, prev_qsigs", row['rid'], index, prev_ratio, prev_match_ratio,  prev_match_secs, prev_qsigs, prev_index)
                        present = 1
                if present == 0:
                    #print ("unique value", row['rid'])
                    duplicate_rows[chan_start] = (score, chan_start, chan_start + row['ref_duration'], ratio, match_ratio, match_secs, qsigs, index)
    except Exception as e:
        print("Error will saving to server, retrived_results:", retrieved_results, "error:", e)
    #Print all duplicate keys
        #For each duplicate key
    #find best score
    #set best index in each row = best index
    for key in duplicate_rows.keys():
        best_score = 0
        best_index = -1
        print("dupl", duplicate_rows[key])

    for index in range(len(results_list)):
        best_score = 0
        best_index = -1
        row = results_list[index]
        print("index->", row)
        chan_start = int(row['chan_start'])
        ratio = float(int(cnt)/min(int(row['ref_duration']), 900))*1000
        match_secs = int(row['match_secs'])
        match_ratio = float((match_secs/min(row['ref_duration'], 900))/1000.0)
        qsigs = int(row['qsigs'])
        cnt = int( row['cnt'] )

        prev_ratio, prev_match_ratio, prev_match_secs, prev_qsigs, prev_index = 0, 0, 0, 0, -1
        ref_duration = results_list[index]['ref_duration']
        if (ref_duration > 17000 and ref_duration < 32000):
            lvar=1.07
        elif (ref_duration  > 32000 and ref_duration  < 64000):
            lvar=1.14
        elif (ref_duration  > 64000 and ref_duration < 128000):
            lvar = 1.2
        elif (ref_duration  > 128000 and ref_duration < 305000):
            lvar = 1.25
        else:
            lvar = 1.35
        score = lvar * (float(match_secs/float(min(ref_duration,900)/1000.0)) * mvar + match_ratio \
                        + float(qsigs/float(min(ref_duration,900)/1000)) * qvar )    
        best_match = 0  
        tested = 0
        not_best = 0
        for already_present_chan_start in duplicate_rows.keys():
            duration = 0
            duplicate = 0
            tested = 1
           
            best_score, d_q_start, d_q_end, prev_ratio, prev_match_ratio, prev_match_secs, prev_qsigs, prev_index = duplicate_rows[already_present_chan_start]
            if (1) : #int(row['ref_duration']) > 120000 or d_q_end - d_q_start > 120000:
                duration = int(row['ref_duration'])
                overlap = min(int(row['ref_duration']+chan_start), int(d_q_end)) - max(chan_start, int(d_q_start))
                if int(row['ref_duration']) < int(d_q_end) - int(d_q_start):
                    if overlap > 0.4 * (row['ref_duration']):
                          duplicate = 1
                else:
                    if overlap > 0.4 * (int(d_q_end) - int(d_q_start)):
                          duplicate = 1
           
            if (((chan_start >= (already_present_chan_start-overlap_period)) and (chan_start <= (already_present_chan_start + overlap_period)) or duplicate == 1 ) ) \
             or  ((chan_start < (d_q_end-overlap_period) and (chan_start + ref_duration) > (d_q_start + overlap_period) ) ):  
                not_best = 1
                if index == prev_index:
                    best_match = 1
        if (best_match == 0) and ((best_match == 0 and tested == 1 and not_best == 1) or not_best == 1):  
            results_list[index]['valid'] = 0.5
    # print("Results : Duration {}-{} ", adObj.start_hour, adObj.end_hour)
    print(duplicate_rows)
    for row in results_list :
        print(row)
   
    return results_list

#  Function for ad database (Main function of the code)


"""### FAST API"""

#class for input to the API
class DataModelIn(BaseModel):
    '''
    Used to Read inputs from the User
    '''
    fps: List[dict]

class InputDataException(Exception):
    def __init__(self, data: str):
        self.data = data


@app.exception_handler(InputDataException)
async def input_data_exception_handler(request: Request, exc: InputDataException):
    sample_fps = [{"timestamps": 400, "fingerprints": "0x062e", "id": "GAC"}, {"timestamps": 500, "fingerprints": "0x1866", "id": "GAC"}, {"timestamps": 600, "fingerprints": "0x196d", "id": "GAC"}]
    return JSONResponse(
        status_code=422,
        content={"message": f"Oops! fps: {exc.data} not in proper format \n sample fps: {sample_fps}"},
    )


#main function
@app.post("/v1/ad_detect_search")
async def ads_database_search_main(data: DataModelIn = Body(...)): #adObj , start_timestamp , end_timestamp , collection_name , debug ) :
    '''
    Calls audio_stage1 query, filter, verify query and save the results on server.

    input :
            query_id : Network name.
            start_time : start timestamp inside the collection, from where to run the ad-detect queries.
            max_time : max timestamps inside the collection till where to run the ad-detect queries.
            date : date for which to run the pipeline.
            start_hour_of_date : start time of the interval.
            end_hour_of_date : end time of the interval.
            base_path : Path to store the files on server.

    '''

    '''
    Call Audio_stage1 query.
    '''

    #print fps from DataModelIn class
    fps = data.fps

    #check the input passed
    if not isinstance(fps,list) or len(fps)==0 :
        raise InputDataException(data = fps)
    try:
        #check if the id  passed is int not channel name , if its not channel name then assign a channel name
        id_passed = fps[0]["id"]
        if id_passed.isdigit():
            channel_name = 'MTVC'
            #change the id in fps
            for i in fps:
                i['id']='MTVC'
        else:
            channel_name = id_passed
   
        fps_sort = sorted(fps, key=lambda x: x["timestamps"])
        # print(fps_sort)
        #print start and end timestamp from sorted fps list
        start_timestamp = fps_sort[0]["timestamps"]

        end_timestamp = fps_sort[-1]["timestamps"]
    except KeyError:
        raise InputDataException(data = fps)

    except IndexError:
        raise InputDataException(data = fps)

    #steps to do:
    adObj = UpdatAdObj(channel_name, adBreaksStart = start_timestamp, adBreakEnd = end_timestamp)
    selfdf = ads_stage1_search_filter( adObj, start_timestamp , end_timestamp , fps,debug=True )
    #add_docs_to_audioStage1( adObj, str(collection_name))
    time.sleep(1)

    '''
    Call audio_filter and audio_verify query.
    '''
    #print("filtered results: {}".format(selfdf))
    # print(adObj.client)
    verified_result = verify_ads_ad_detect(selfdf, adObj, fps ,debug = True)
    #filter_and_verify_audio_matches( adObj, collection_name )
    #time.sleep(0.1)
    #print("verified final results: {}".format(verified_result))
    #return verified_result
    final_results = []
    # UpdatAdObj(channel_name, adBreaksStart = start_timestamp, adBreakEnd = end_timestamp, verified_result = verified_result)
    if verified_result:
        final_results = save_to_server(adObj, verified_result= verified_result)
   
    return final_results
 


if __name__ == '__main__':
    uvicorn.run(app, port=8085, host="0.0.0.0")#, reload=True)
