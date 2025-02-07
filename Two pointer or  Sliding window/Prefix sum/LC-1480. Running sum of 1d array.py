class Solution:
    def runningSum(self, nums: List[int]) -> List[int]: # type:ignore
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
        '''
        We can solve this problem by using prefix sum technique.
        We will iterate over the array and keep adding the previous element to the current element.
        we can initialise another array to store the running sum.
        p = [0]*len(nums)
        p[0] = nums[0]
        for i in range(1, len(nums)):
            p[i] = p[i-1] + nums[i]
        return p
        time complexity: O(N)
        space complexity: O(N)
        '''
    # Time complexity: O(N)
    # Space complexity: O(1)
    
    