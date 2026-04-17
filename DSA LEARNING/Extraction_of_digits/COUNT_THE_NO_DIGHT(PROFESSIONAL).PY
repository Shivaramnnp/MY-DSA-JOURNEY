from math import *
def CountDigits(num):
   return int(log10(num)+1)
no = 12345
print(CountDigits(no))

#Time complexity = O(1)
#space complexity = (1)