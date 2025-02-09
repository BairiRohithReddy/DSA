# product of array except self
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
# Here is the solution:
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]: # type:ignore
#         '''
#         We can solve this problem by using prefix sum technique.
#         We will create two arrays left and right of size n.
#         We will initialize left[0] and right[n-1] as 1.
#         We will calculate the prefix sum of the left array.
#         We will calculate the prefix sum of the right array.
#         Finally we will return the product of left and right arrays.
#         time complexity: O(N)
#         space complexity: O(N)
#         '''
#         n = len(nums)
#         left = [1]*n
#         right = [1]*n
#         for i in range(1,n):
#             left[i] = left[i-1]*nums[i-1]
#         for i in range(n-2,-1,-1):
#             right[i] = right[i+1]*nums[i+1]
#         return [left[i]*right[i] for i in range(n)]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # type:ignore
        '''
        we will now solve this using prefix sum technique.
        Instead of creating two arrays which take up additional space 
        we will use a single array to keep track of the prefix sum.
        and then multiply the postfix after we calculate it
        this will give us a space complexity of O(1)
        '''
        n = len(nums)
        res = [1]*n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    