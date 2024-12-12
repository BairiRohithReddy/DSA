from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the number that appears only once in a list where all other numbers appear twice.

        This method implements two approaches:
        1. Using a Counter (hash map)
        2. Using XOR operation (commented out)

        Args:
        nums (List[int]): A list of integers where all numbers except one appear twice.

        Returns:
        int: The number that appears only once, or None if not found.
        """

        # Approach 1: Using Counter
        """
        We create a hash map (Counter) of numbers and their frequencies.
        Then we find the number with a frequency of 1.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        temp_nums = Counter(nums)
        for num, count in temp_nums.items():  # .items() was missing in the original code
            if count == 1:
                return num
        return None  # Return None if no single number is found

        # Approach 2: Using XOR (commented out)
        """
        XOR all elements together. Numbers appearing twice will cancel out (a XOR a = 0),
        leaving only the number that appears once.
        Time Complexity: O(n), Space Complexity: O(1)
        
        result = 0
        for num in nums:
            result ^= num  # XOR operation (^=) instead of assignment (=)
        return result
        """
