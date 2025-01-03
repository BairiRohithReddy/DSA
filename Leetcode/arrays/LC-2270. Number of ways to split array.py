class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int: # type:ignore
        """
        Count the number of ways to split the array into two non-empty subarrays,
        where the sum of elements in the left subarray is greater than or equal to
        the sum of elements in the right subarray.

        Args:
        nums (List[int]): The input array of integers.

        Returns:
        int: The number of valid ways to split the array.

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1), as it uses constant extra space.
        """
        valid_splits = 0  # Counter for valid splits
        right_sum = sum(nums)  # Initial sum of all elements
        left_sum = 0  # Initial sum of left subarray (empty at start)

        # Iterate through the array, considering each possible split point
        for i in range(len(nums) - 1):  # Stop at second-to-last element
            left_sum += nums[i]  # Add current element to left sum
            right_sum -= nums[i]  # Remove current element from right sum

            # Check if current split is valid
            if left_sum >= right_sum:
                valid_splits += 1  # Increment counter if valid

        return valid_splits  # Return total count of valid splits
