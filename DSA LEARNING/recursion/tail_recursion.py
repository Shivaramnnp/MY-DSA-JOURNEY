def tail_recursion(n: int) -> None:


    if n <= 0:
        return


    print(n)


    tail_recursion(n - 1)



if __name__ == "__main__":
    print("Tail Recursion Output:")
    tail_recursion(5)