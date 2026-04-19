def prime(num):

    if num <= 1:
        return "NOT prime"

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "NOT prime"

    return "PRIME"


no = 13
print(prime(no))