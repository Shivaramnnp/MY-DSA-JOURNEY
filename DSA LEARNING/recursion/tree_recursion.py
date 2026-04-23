def fibonacci(n: int) -> int:

    if n <= 1:
        return n


    return fibonacci(n - 1) + fibonacci(n - 2)



if __name__ == "__main__":
    print("Tree Recursion Output (Fibonacci):")

    for i in range(6):
        print(f"Fibonacci({i}) =", fibonacci(i))