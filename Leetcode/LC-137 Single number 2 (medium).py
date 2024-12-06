from typing import List
class Solution:
    def singleNumber(self, nums:List[int])->List[int] :
        '''
        Find the element that appears exactly once in an array where every other element appears three times.

        Given an integer array `nums` where every element appears three times except for one, which appears exactly once,
        this function returns the single number.

        The algorithm must have a linear runtime complexity and use constant space.
        
        This approach uses counting the bits at each position to construct the required number
        '''
        # result will store the required number
        result = 0
        # we now iterate through all the possible 32 bits
        for i in range(32):
            # bit_sum will store the count of bits at each position
            bit_sum = 0
            for num in nums:
                if num & (1<<i):
                    bit_sum +=1
            if bit_sum % 3 != 0:
                result |= (1 << i)
        # handling the edge case where the 32nd bit is set which indicates the number is negative
        if result >= 2**31:
            result -= 2**32     
        return result