# This program will convert a given decimal number to binary number
def decToBin(n):
    # this function takes an input number and returns its binary representation
    # the best data type to represent a binary form of a number is string
    bin_rep = ""
    while n!=1:
        if n % 2 == 1: bin_rep += "1"
        else: bin_rep += "0"
        n = n//2
        if n == 1:
            bin_rep += "1"
    bin_rep = bin_rep[::-1]
    return bin_rep

n = 5
a = decToBin(n)
print(a)
