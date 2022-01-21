
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. 
# Given a number n, the task is to find n’th Ugly number.

# nth ugly number


# def primeFactors(n):
#     s = set()
#     # Print the number of two's that divide n
#     while n % 2 == 0:
#         s.add(2)
#         n = n / 2
         
#     # n must be odd at this point
#     # so a skip of 2 ( i = i + 2) can be used
#     for i in range(3,int(n**(1/2))+1,2):
         
#         # while i divides n , print i and divide n
#         while n % i== 0:
#             s.add(i)
#             n = n // i
             
#     # Condition if n is a prime
#     # number greater than 2
#     if n > 2:
#         s.add(n)
#     return s
# print(primeFactors(231339))

# def max_divide(a):
#     for b in (2,3,5):
#         while a % b == 0:
#             a = a / b
#     return a

# def nthugly(n):
#     i = 0
#     uc = 0
#     while uc<n:
#         i += 1
#         #divide i by greatest divisible powers of 2,3,5
#         k = max_divide(i)
#         if k==1:
#             uc += 1
#     return i
 
# print(nthugly(150))




# def u(n):
#     dp = [1,2,3]
#     for i in range(3,n+1):
#         print(dp)
#         s = a
#         a = []
#         for j in s:
#             a.append(j*2)
#             a.append(j*3)
#             a.append(j*5)
#         dp += set
    
#     for a in dp[::-1]:
#         if a<=n:
#             return a

# # for i in range(1,15):
# print(u(10))

def getNthUglyNo(n):
 
    ugly = [0] * n  # To store ugly numbers
 
    # 1 is the first ugly number
    ugly[0] = 1
 
    # i2, i3, i5 will indicate indices for
    # 2,3,5 respectively
    i2 = i3 = i5 = 0
 
    # Set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
 
    # Start loop to find value from
    # ugly[1] to ugly[n]
    for l in range(1, n):
        # Choose the min value of all
        # available multiples
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)
 
        # Increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
 
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
 
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
 
    # Return ugly[n] value
    return ugly[-1]

# getNthUglyNo(17)
# another way to do this is to use a binary search algo from 0, intmax