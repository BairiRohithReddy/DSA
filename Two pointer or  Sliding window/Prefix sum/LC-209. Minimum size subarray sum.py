class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: #type:ignore
        l = 0
        curr_total = 0
        min_len = float('inf')
        
        for r in range(len(nums)):
            curr_total += nums[r]
            while total >= target:
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l +=1
        return 0 if min_len == float('inf') else min_len
    '''
    we can solve this problem by using sliding window technique.
    we will initialise two pointers l and r to 0.
    we will initialise a variable curr_total to 0.
    we will initialise a variable min_len to float('inf').
    we will iterate over the array using r.
    we will update the curr_total by adding the rth element.
    we will iterate over the array using l.
    we will update the min_len by taking the minimum of min_len and r-l+1.
    we will update the curr_total by subtracting the lth element.
    we will increment the l pointer.
    finally we will return 0 if min_len is float('inf') else min_len.
    time complexity: O(N)
    space complexity: O(1)
    '''    