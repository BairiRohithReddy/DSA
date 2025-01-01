class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        Calculate the sum of all integers in the range [1, n] that are divisible by 3, 5, or 7.

        Args:
        n (int): The upper bound of the range (inclusive).

        Returns:
        int: The sum of all multiples of 3, 5, or 7 in the range [1, n].

        Approach:
        - Iterate through the range from 1 to n (inclusive).
        - For each number, check if it's divisible by 3, 5, or 7.
        - If divisible, add it to the running sum.

        Time Complexity: O(n), where n is the input number.
        Space Complexity: O(1), as we only use a constant amount of extra space.

        Note:
        This approach checks each number individually, which is straightforward
        but may not be the most efficient for very large values of n.
        For larger inputs, mathematical optimizations using the inclusion-exclusion
        principle or arithmetic progressions could be considered.
        """

        result = 0
        for i in range(1, n+1):
            if i % 3 == 0:
                result += i  # Add multiples of 3
            elif i % 5 == 0:
                result += i  # Add multiples of 5
            elif i % 7 == 0:
                result += i  # Add multiples of 7

        return result
