def head_recursion(n: int) -> None:
    if n <= 0:
        return

    head_recursion(n - 1)
   
    print(n)



if __name__ == "__main__":
    print("Head Recursion Output:")
    head_recursion(5)