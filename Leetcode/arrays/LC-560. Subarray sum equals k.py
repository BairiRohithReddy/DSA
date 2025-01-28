class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: #type:ignore
        prefix_sum = defaultdict(int)   #type:ignore
        prefix_sum[0] = 1   #base case where the sum of the subarray is equal to k
        count = 0
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            count += prefix_sum[curr_sum-k]
            prefix_sum[curr_sum] += 1
        return count
    
'''
intution:
we are using a dictionary to store the prefix sum of the array.
we are iterating through the array and calculating the prefix sum of the array.
if the difference between the current prefix sum and k is present in the dictionary, then we have found a subarray with sum equal to k.
Time complexity: O(n); Space complexity: O(n)
'''

#approach 2 but this lead to TLE due to the nested loop with O(n^2) time complexity

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: #type:ignore
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count
'''
intution:
we are using two nested loops to iterate through the array.
the outer loop is used to fix the starting index of the subarray.
the inner loop is used to fix the ending index of the subarray.
we are calculating the sum of the subarray and checking if it is equal to k.
Time complexity: O(n^2); Space complexity: O(1)
'''

#approach 3 using prefix sum and hashmap
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: #type:ignore
        count = 0
        count = 0
        sum = 0
        dic = {0:1}
        for i in nums:
            sum += i
            if sum - k in dic:
                count += dic[sum-k]
            if sum in dic:
                dic[sum] += 1
            else:
                dic[sum] = 1
        return count
'''
intution:
we are using a dictionary to store the prefix sum of the array.
we are iterating through the array and calculating the prefix sum of the array.
if the difference between the current prefix sum and k is present in the dictionary, then we have found a subarray with sum equal to k.
Time complexity: O(n); Space complexity: O(n)
'''
        