from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        Find the maximum length of a subsequence where all elements can be made equal.

        This function determines the longest subsequence in 'nums' where all elements
        can be made equal by replacing each element with any value in the range
        [nums[i] - k, nums[i] + k].

        Args:
        nums (List[int]): A list of integers.
        k (int): The range within which each element can be modified.

        Returns:
        int: The length of the longest subsequence that can be made equal.

        Algorithm:
        1. Sort the list to have elements in ascending order.
        2. Use a sliding window approach to find the longest valid subsequence.
        3. Expand the window as long as the difference between the largest and
           smallest elements is within 2*k.
        4. If the difference exceeds 2*k, shrink the window from the left.
        5. The final window size is the length of the longest valid subsequence.
        """

        # Sort the list in ascending order.
        # This makes it easier to check for common elements in successive ranges.
        nums.sort()

        # Initialize the left pointer of the sliding window
        i = 0

        # Iterate through the list with the right pointer j
        for j in range(len(nums)):
            # Check if the difference between the current element (j) and
            # the leftmost element (i) exceeds the allowed range (2*k)
            if nums[j] - nums[i] > 2*k:
                # If exceeded, move the left pointer to shrink the window
                i += 1

        # The length of the valid subsequence is the final window size
        return j - i + 1

# Test case
solution = Solution()
nums = [1, 4, 5, 7, 9]
k = 2
result = solution.maximumBeauty(nums, k)
print(f"Input: nums = {nums}, k = {k}")
print(f"Output: {result}")
print("Explanation: The longest subsequence that can be made equal is [4, 5, 7].")
print("We can modify 4 to 6, 5 to 6, and 7 to 6 to make them all equal.")


'''
# My Notes
we have sorted this list we have all the elements in the ascending order and now we are adding k 
to the smallest number which is  at index i and subtracting from element at index j by doing 
this we are essentially trying to find if their difference is less than 2 * k, if it is less 
than or equal to 2*k then both the elements have a common element in the range of A[i]+-k, 
and hence will form a subsequence. if they fail this condition then we increment i 

since we need the length of the subsequence, once all the elements are iterated through we 
find the length by subtracting the i from j and add 1 so we get the length
'''