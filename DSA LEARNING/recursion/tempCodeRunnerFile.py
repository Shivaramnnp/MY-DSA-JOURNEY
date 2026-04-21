#print shiva 4 times using recursion
def func(count):
    if count == 4:
        return
    print("hello, shiva")
    func(count + 1)

func(0)
