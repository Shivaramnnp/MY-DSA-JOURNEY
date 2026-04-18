# THIS IS OPTIMAL SOLUTION WHERE REDUSE TIME COMPLEXITY 
from math import sqrt
def factor(num):
    result = []
    for i in range(1, int(sqrt(num))):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num//i)
    result.sort()
    return result
no = 36
print(factor(36))


# TC = O(sqrt(n)) + O(nlogn)
# SC = O(k) where k is parameter