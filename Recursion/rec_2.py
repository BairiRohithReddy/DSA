# In this example we shall print numbers from 1 to n linearly using recursion and then print numbers in the reverse order from n to 1 linearly
def printNumbers(i, n):
    # part-1 print the numbers from 1 to n linearly
    # if i > n:
    #     return
    # print(i)
    # printNumbers(i+1, n)
    # part-2 print the numbers from n to 1 linearly
    if i < 1:
        return
    print(i)
    printNumbers(i-1, n)
    
#a = printNumbers(1, 5) # part-1
a = printNumbers(5, 5) # part-2