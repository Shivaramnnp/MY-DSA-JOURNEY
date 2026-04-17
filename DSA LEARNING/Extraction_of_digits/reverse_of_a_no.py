def reverseOfNum(num):
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        num = num//10

no = 1234
reverseOfNum(no)
