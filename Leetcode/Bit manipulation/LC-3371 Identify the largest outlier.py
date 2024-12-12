from typing import List
from collections import Counter
from math import inf

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        Find the largest outlier in a list of integers.

        An outlier is defined as a number that, when removed, makes the average
        of the remaining numbers an integer.

        Intuition:
        If a number is an outlier, the sum of the remaining numbers must be even
        and divisible by the count of remaining numbers (n-1).

        Args:
        nums (List[int]): A list of integers.

        Returns:
        int: The largest outlier in the list, or -inf if no outlier exists.

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n) for the Counter object.
        """
        
        # Calculate the sum of all numbers in the list
        num_sum = sum(nums)
        
        # Create a frequency counter for the numbers in the list
        freq = Counter(nums)
        
        # Initialize the outlier to negative infinity
        outlier = -inf
        
        # Iterate through each number in the list
        for i in nums:
            # Calculate the sum of remaining numbers if i is removed
            req_sum = num_sum - i
            
            # Check if the remaining sum is even
            if req_sum % 2 == 0:
                # Calculate the required average
                req_sum //= 2
                
                # Check if the required average exists in the list
                # and it's not the same as i (or if it is, there's more than one of it)
                if req_sum in freq and (i != req_sum or freq[req_sum] > 1):
                    # Update the outlier if this number is larger
                    outlier = max(outlier, i)
        
        # Return the largest outlier found (or -inf if none found)
        return outlier
