class Solution:
    def pivotIndex(self, nums: List[int]) -> int: #type:ignore
        """
        Find the pivot index in the given list of numbers.

        The pivot index is the index where the sum of all numbers to the left
        of the index is equal to the sum of all numbers to the right of the index.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The pivot index if it exists, -1 otherwise.
        """

        def approach1(nums: List[int]) -> int: #type:ignore
            """
            First approach: Brute force method.

            Iterates through each index, calculating left and right sums for each.

            Time Complexity: O(n^2), where n is the length of nums.
                             We iterate n times, and for each iteration, we sum up to n elements.
            Space Complexity: O(1), as we only use a constant amount of extra space.

            Returns:
                int: The pivot index if found, -1 otherwise.
            """
            for i in range(len(nums)):
                left_sum = sum(nums[:i])  # Sum of elements to the left of i
                right_sum = sum(nums[i+1:])  # Sum of elements to the right of i
                if left_sum == right_sum:
                    return i  # Pivot index found
            return -1  # No pivot index found

        def approach2(nums: List[int]) -> int: #type:ignore
            """
            Second approach: Optimized method using cumulative sum.

            Calculates total sum once and then uses running left sum to find pivot.

            Time Complexity: O(n), where n is the length of nums.
                             We iterate through the list once to calculate total sum,
                             and once more to find the pivot index.
            Space Complexity: O(1), as we only use a constant amount of extra space.

            Returns:
                int: The pivot index if found, -1 otherwise.
            """
            total_sum = sum(nums)  # Calculate total sum once
            left_sum = 0
            for i, n in enumerate(nums):
                right_sum = total_sum - left_sum - n  # Calculate right sum
                if left_sum == right_sum:
                    return i  # Pivot index found
                left_sum += n  # Update left sum for next iteration
            return -1  # No pivot index found

        # Uncomment the approach you want to use
        # return approach1(nums)
        return approach2(nums)
