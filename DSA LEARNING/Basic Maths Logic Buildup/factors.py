def factor(num):
    n = num
    result = []
    for i in range(1, n):
        if n % i == 0:
         result.append(i)
    result.append(num)
    return result
no = 25
print(factor(no))


#tc = O(n)
#sc = o(k) where k is parameter
