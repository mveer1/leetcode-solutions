def ansmemo1(s, sum, memo={}):
    # print(sum)
    if sum in memo: return memo[sum]
    if sum==0: 
        # print("r0")
        return 1

    count = 0
    for i in s:
        rem = sum - i
        if rem>=0:
            res = ansmemo1(s, rem, memo)
            if res:
                # print(memo)
                count+=1

    memo[sum] = count
    return count
    

# print(ans(s, sum))
# print(ans([1,2,3,4,5,6], 100))
# print(ansmemo1(s, sum))
# print(ansmemo1([1,2,3,5,6], 9))
print(ansmemo1([1,2,3,4,5,6,7,8,9], 14))