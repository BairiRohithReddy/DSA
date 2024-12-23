class Solution:
    def findMin(self, nums: List[int]) -> int: #type:ignore
        """
        Find the minimum element in a rotated sorted array.

        This function uses a modified binary search algorithm to find the minimum
        element in an array that was originally sorted in ascending order and then
        rotated at some pivot unknown to you beforehand.

        Args:
            nums (List[int]): A list of integers representing the rotated sorted array.

        Returns:
            int: The minimum element in the array.

        Time Complexity:
            O(log n), where n is the length of nums. We perform a binary search,
            halving the search space in each iteration.

        Space Complexity:
            O(1), as we only use a constant amount of extra space regardless of input size.
        """
        # Edge case: if array has only one element, it's the minimum
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums) - 1
        
        # If the last element is greater than the first element, array is not rotated
        if nums[high] > nums[0]:
            return nums[0]

        # Binary search loop
        while low < high:
            mid = (low + high) // 2
            
            # If mid element is greater than high element, minimum is in the right half
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # If mid element is less than or equal to high element,
                # minimum is in the left half, including mid
                high = mid
        
        # When low and high converge, we've found the minimum element
        return nums[low]
