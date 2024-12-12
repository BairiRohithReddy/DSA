class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: #type:ignore
        """
        Find the maximum number of consecutive 1's in the binary array.

        Args:
        nums (List[int]): A binary array containing only 0's and 1's.

        Returns:
        int: The length of the longest contiguous segment of 1's.

        Time Complexity: O(n), where n is the length of the input array.
        Space Complexity: O(1), using only a constant amount of extra space.
        """
        
        max_ones = 0  # Variable to store the maximum count of consecutive 1's
        count = 0     # Variable to keep track of the current count of consecutive 1's
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1  # Increment count when we encounter a 1
            else:
                count = 0   # Reset count to 0 when we encounter a 0
            
            # Update max_ones if current count is greater
            max_ones = max(count, max_ones)
        
        return max_ones