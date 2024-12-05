def printNTimes(i,n):
    # this funciton will take a number n and a name and will print the name n times
    if i > n :
        return
    print("Rohith", i)
    printNTimes(i+1, n)

a = printNTimes(1,5)
