def Palindrome(num):
    num = n
    result = 0
    while num > 0:
        ld = num % 10
        result = (result * 10)+ld
        num = num // 10
    if n == result:
        return " Palindrome "
    else:
        return "Not a  Palindrome"
n = 121
print(Palindrome(n))

#tc = O(log10(n))
#SC = O(1)