from typing import Optional
class Solution:
     def countPrimes(self, n):
         if n<2:
             return 0 # as there are no primes less than 2 and 2 is the smallest prime 
         primes = [True] * n #this will create an array of size n and tracks whether the numbers are prime or not using bools
         primes[0] = primes[1] = False # we know that the smallest prime number is 2 so we assign 0,1 false
         for i in range(2, int(n**(0.5))+1):
             # this for is used for primes from 2 to the sqrt of the upper limit
             if primes[i]:
                 # this checks if the number is prime
                 for j in range(i*i, n, i):
                     # as we start from 2 we will weed out all the composite numbers that are multiples of 2
                     # then we do the same with 3 and so on till sqrt(n)
                     # so we only need to check from i*i as i*2 is already handled by 2*i, similarly i*3 by 3*i, we do this till n in the increments of i
                     primes[j] = False
                     # this will mark the composites
         return sum(primes)