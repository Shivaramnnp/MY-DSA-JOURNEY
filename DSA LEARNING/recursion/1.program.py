#print shiva 4 times using recursion
def print_shiva(n):

    if n == 0:      
        return

    print("shiva")  
    print_shiva(n-1)  

