
def countDigit(num):
    count = 0
    while(num > 0):
        last_digit = num % 10
        count +=1
        num = num//10
    return count

no = 12345
print(countDigit(no))

#Time complexity = O(log10(N))
#space complexity = (1)