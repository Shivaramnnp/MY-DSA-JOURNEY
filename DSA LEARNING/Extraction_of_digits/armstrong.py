# Armstrong number check
def armstrong(num):
    n = num
    nod = len(str(num))
    total = 0
    while num > 0:
          ld = num % 10
          total += (ld ** nod)
          num = num // 10
   
    if n == total:
        return "TRUE"
    else:
        return "FALSE"
    
no = 153
print(armstrong(no))

#tc = O(log10(n))
#sc = O(1)