fh = open("tokens.txt", 'r')
subject, verb, predicate, adjective, article = {},{},{},{},{},{}   #make 5 sets

dict = {}
for line in fh:
    setname, item = line.split(":")
    dict[setname].append(item)
print(dict)
