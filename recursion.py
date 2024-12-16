# def rec(n, cnt = 0):
#     if cnt == n:
#         return
#     print(cnt)
#     cnt += 1
#     rec(n, cnt)

# print("print 0 to n-1")    
# rec(5)

# # common recursion patterns
# '''
# 1. Print numbers from 0 to n or n to 1
# 2. Factorial!.
# 3. Fibonacci Sequence
# '''

# # print numbers from 0 to n
# def nto1(n):
#     if n < 0: return
#     print(n)
#     n -= 1
#     nto1(n)
    
# print("Print n to 0")
# nto1(5)
    
# def zeroton(n, low = 0):
#     if low > n: return
#     print(low)
#     low += 1
#     zeroton(n, low)
    
# print("print zero to n")
# zeroton(5)

# # factorial of n. n!

# def nfactorial(n):
#     if n == 0 or n ==1 : return 1
#     return n * nfactorial(n-1)

# n = 5
# factn = nfactorial(5)
# print(f'Factorial of {n} is, {factn}')

# # fibonacci sequence

# def fibo(n):
#     if n <= 1: return 1
#     return fibo(n-1) + fibo(n-2)

# def fibo_count(count):
#     seq = []
#     for i in range(count):
#         seq.append(fibo(i))
#     return seq

# n = 20
# fibonacci_seq = fibo_count(n)
# print(f'Fibonacci sequence of {n} numbers is, {fibonacci_seq}')

# sum of first n numbers
# using parameterised method
def firstNnumbersSum(n, sum):
    if n < 1:
        print(sum)
        return
    firstNnumbersSum(n-1, sum + n)

firstNnumbersSum(5,0)

# without using parameters

def naturalnsum(n):
    if n == 0: return 0
    return n + naturalnsum(n-1)

print(naturalnsum(5))

# product of first n natural numbers
def productN(n):
    if n == 1:return 1
    return n * productN(n-1)

print(productN(5))