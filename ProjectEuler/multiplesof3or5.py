'''
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3,5,6 and 9. the sum of these multiples is 23
find the sum of all the multiples of 3 or 5 below 1000
'''

def multiplesof3or5():
    total = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(multiplesof3or5())