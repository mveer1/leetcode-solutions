# The Unix epoch (or Unix time or POSIX time or Unix timestamp) 
# is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds
# sample value = 1621583985.0666816

# Creating a sample
test = []
import time, random
for _ in range(10):
    test.append(str(time.time()))      #storing them as string
    time.sleep(.5)              #to get unique timestamps in interval of 0.5 seconds

random.shuffle(test)

# Now sorting that sample

# Using Timsort, hybrid of merge and insertion, O(nlogn)time, O(n)space, stable
sortedtest = sorted(test, key= lambda x:float(x), reverse=False)

# Printing it
for i in range(len(test)):
    print(test[i], f"<{i}>", sortedtest[i])