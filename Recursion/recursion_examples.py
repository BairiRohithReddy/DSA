# # # # # def rec(n, cnt = 0):
# # # # #     if cnt == n:
# # # # #         return
# # # # #     print(cnt)
# # # # #     cnt += 1
# # # # #     rec(n, cnt)

# # # # # print("print 0 to n-1")    
# # # # # rec(5)

# # # # # # common recursion patterns
# # # # # '''
# # # # # 1. Print numbers from 0 to n or n to 1
# # # # # 2. Factorial!.
# # # # # 3. Fibonacci Sequence
# # # # # '''

# # # # # # print numbers from 0 to n
# # # # # def nto1(n):
# # # # #     if n < 0: return
# # # # #     print(n)
# # # # #     n -= 1
# # # # #     nto1(n)
    
# # # # # print("Print n to 0")
# # # # # nto1(5)
    
# # # # # def zeroton(n, low = 0):
# # # # #     if low > n: return
# # # # #     print(low)
# # # # #     low += 1
# # # # #     zeroton(n, low)
    
# # # # # print("print zero to n")
# # # # # zeroton(5)

# # # # # # factorial of n. n!

# # # # # def nfactorial(n):
# # # # #     if n == 0 or n ==1 : return 1
# # # # #     return n * nfactorial(n-1)

# # # # # n = 5
# # # # # factn = nfactorial(5)
# # # # # print(f'Factorial of {n} is, {factn}')

# # # # # # fibonacci sequence

# # # # # def fibo(n):
# # # # #     if n <= 1: return 1
# # # # #     return fibo(n-1) + fibo(n-2)

# # # # # def fibo_count(count):
# # # # #     seq = []
# # # # #     for i in range(count):
# # # # #         seq.append(fibo(i))
# # # # #     return seq

# # # # # n = 20
# # # # # fibonacci_seq = fibo_count(n)
# # # # # print(f'Fibonacci sequence of {n} numbers is, {fibonacci_seq}')

# # # # # sum of first n numbers
# # # # # using parameterised method
# # # # def firstNnumbersSum(n, sum):
# # # #     if n < 1:
# # # #         print(sum)
# # # #         return
# # # #     firstNnumbersSum(n-1, sum + n)

# # # # firstNnumbersSum(5,0)

# # # # # without using parameters

# # # # def naturalnsum(n):
# # # #     if n == 0: return 0
# # # #     return n + naturalnsum(n-1)

# # # # print(naturalnsum(5))

# # # # # product of first n natural numbers
# # # # def productN(n):
# # # #     if n == 1:return 1
# # # #     return n * productN(n-1)

# # # # print(productN(5))

# # # # reverse a given array of integers
# # # # normal approach would be to use 2 pointers i=0, j = len(arr)-1 and then swap i and j then increment i and decrement j
# # # # until i >= j. 

# # # # def reverse_arr(nums, i = 0, j = None):
# # # #     if j is None:
# # # #         j = len(nums)-1
# # # #     if i >= j: return nums
# # # #     nums[i], nums[j] = nums[j], nums[i]
# # # #     return reverse_arr(nums, i+1, j-1)
    
# # # # print('using two pointers')
# # # # nums = [1,2,3,4,5]
# # # # print(reverse_arr(nums))

# # # # # now reversing the array using a single pointer instead of 2
# # # # # the relation between i and j pointers can be written as j = n-i-1 
# # # # # for example: consider an array of size 5, i=0, j=5-0-1 =4 which is the last index. similarly i=1, j=5-1-1 = 3 

# # # # def rev_arr(nums, i = 0):
# # # #     if i>len(nums)/2: return nums
# # # #     nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
# # # #     return rev_arr(nums, i+1)

# # # # nums = [6,5,4,3,2,13]
# # # # print('using single pointer')
# # # # print(rev_arr(nums))

# # # # check if a given string is a palindrome or not

# # # def palin(user_text, i = 0):
# # #     if i>len(user_text)/2: return True
# # #     if user_text[i] != user_text[len(user_text)-i-1]:
# # #         return False
# # #     return palin(user_text, i+1)

# # # user_text = 'madam'
# # # print(palin(user_text))

# # # Multiple Recursion calls

# # def fibonacci_number(n):
# #     if n<=1:
# #         return n
# #     first = fibonacci_number(n-1)
# #     last = fibonacci_number(n-2)
# #     return first + last

# # print(fibonacci_number(10))

# # Print all the subsequences
# '''
# a contiguous or non contiguous sequences which follows the order
# consider an array [3,1,2] and the possible subsequences are
# all the following are subarrays except for 3,2, a subarray can be a subsequence
# 3
# 1
# 2
# 3,1
# 3,2 but this is not a subarray, in order to be a subsequence the order has to be maintained.
# 1,2
# 3,1,2
# '''
# def subseq(idx, arr, temp=None):
#     if temp is None:
#         temp = []
        
#     if idx >= len(arr):
#         return [temp[:]]
    
#     temp.append(arr[idx])
#     include = subseq(idx+1, arr, temp)
#     temp.pop()
#     exclude = subseq(idx+1, arr, temp)
#     return include + exclude
    
# arr = [3,1,2]
# print(subseq(0, arr))

# printing subsequences whose sum is k
def subsumk(i, arr, req_sum, temp=None, temp_sum =None):
    if temp is None:
        temp = []
        
    if temp_sum is None:
        temp_sum = 0
        
    if i == len(arr):
        if temp_sum == req_sum:
            return temp
            
    temp.append(arr[i])
    temp_sum += arr[i]
    result = subsumk(i+1, arr, req_sum, temp, temp_sum)
    if result:
        return result
    temp.pop()
    return subsumk(i+1, arr, req_sum, temp, temp_sum)
    
arr = [3,1,2]
req_sum = 3
print(subsumk(0, arr, req_sum))

