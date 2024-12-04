# now we shall implement another program that converts binary to decimal representation
def binToDec(n):
    str_len = len(n)
    # since 2^0 is 1 which is the first power of 2 we assign 1 to power_2
    power_2 = 1
    # we shall initialise a num as 0 which will be used to compute the required number 
    num = 0
    # since we are taking from 2 power 0 which is the right most bit we traverse the string from right to left
    # so the index of the last bit will be len of string -1 and the final index 0 is also included so it goes till -1 which is not inclusive in steps of -1
    # then after calculating for every bit position we will increase the power_2 by 2 times 
    for i in range(str_len-1,-1,-1):
        if n[i] == "1":
            num = num + power_2
        power_2 = power_2 *2
    return num

n = "1001"
print(binToDec(n))