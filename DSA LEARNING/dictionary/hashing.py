def hashing(lst1,lst2):
    for num in lst1:
        count = 0
        for no in lst2:
            if no == num:
                count += 1
        print(num ,"appears" ,count,"times")
m =[1,1,1,1,2,2]
n =[2,1]
hashing(n,m)
# tc = O(m*n)
# O(k)


