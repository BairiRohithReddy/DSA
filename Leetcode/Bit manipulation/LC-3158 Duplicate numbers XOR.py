class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int: # type: ignore
        """
        Find the XOR of all numbers that appear exactly twice in the input list.

        This approach directly performs the XOR operation without using a temporary list.

        Args:
        nums (List[int]): A list of integers where some numbers appear twice.

        Returns:
        int: The XOR of all numbers that appear exactly twice.

        Example:
        >>> s = Solution()
        >>> s.duplicateNumbersXOR([1, 2, 1, 3, 3, 4, 5, 4, 5])
        2
        """
        # Count the frequency of each number
        freq = Counter(nums) # type: ignore
        
        # Variable to store the final XOR result
        result = 0
        
        # Perform XOR operation on numbers that appear twice
        for num, count in freq.items():
            if count == 2:
                result ^= num
        
        return result