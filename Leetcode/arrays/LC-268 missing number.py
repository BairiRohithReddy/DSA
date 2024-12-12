from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number in a sequence of integers from 0 to n.

        Approach 1: Linear Search
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Args:
        nums (List[int]): A list of integers from 0 to n with one number missing.

        Returns:
        int: The missing number, or None if no number is missing.
        """
        # Iterate through the range from 0 to length of nums (inclusive)
        for i in range(len(nums) + 1):
            # Check if the current number is not present in the input list
            if i not in nums:
                # If number is missing, return it immediately
                return i
        
        # Return None if no missing number found (theoretically should not happen)
        return None

    def missingNumberSumApproach(self, nums: List[int]) -> int:
        """
        Find the missing number in a sequence of integers from 0 to n.

        Approach 2: Sum Difference
        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
        nums (List[int]): A list of integers from 0 to n with one number missing.

        Returns:
        int: The missing number.
        """
        # Calculate the length of the input list
        n = len(nums)

        # Calculate the expected sum of all numbers from 0 to n
        # Formula: n * (n + 1) / 2
        # Use integer division (//) to avoid float precision issues
        expected_sum = n * (n + 1) // 2

        # Calculate the actual sum of numbers in the input list
        actual_sum = sum(nums)

        # Return the difference between expected and actual sum
        # This difference is the missing number
        return expected_sum - actual_sum

# Detailed step-by-step walkthrough of both approaches

# Approach 1: Linear Search Example
# Input: [3, 0, 1]
# Steps:
# 1. i = 0: 0 is in the list ✓
# 2. i = 1: 1 is in the list ✓
# 3. i = 2: 2 is NOT in the list ✓ (Return 2)

# Approach 2: Sum Difference Example
# Input: [3, 0, 1]
# Steps:
# 1. n = 3
# 2. expected_sum = 3 * (3 + 1) // 2 = 6
# 3. actual_sum = 0 + 1 + 3 = 4
# 4. missing_number = 6 - 4 = 2

# Example usage and demonstration
solution = Solution()
print("Linear Search Approach:", solution.missingNumber([3, 0, 1]))
print("Sum Difference Approach:", solution.missingNumberSumApproach([3, 0, 1]))