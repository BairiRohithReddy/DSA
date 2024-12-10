class Solution:
    def search(self, nums: List[int], target: int) -> int: # type: ignore
        low, high = 0, len(nums)-1
        while low <=high:
            mid = (low + high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform a binary search on a sorted array to find the target value.

        This method implements the classic binary search algorithm to efficiently
        locate a target value in a sorted array.

        Args:
            nums (List[int]): A sorted list of integers to search through.
            target (int): The value to search for in the list.

        Returns:
            int: The index of the target if found, -1 otherwise.

        Time Complexity: O(log n), where n is the length of the input list.
        Space Complexity: O(1), as it uses only a constant amount of extra space.
        """

        # Initialize the search boundaries
        low, high = 0, len(nums) - 1

        # Continue searching while the boundaries haven't crossed
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            # If the middle element is greater than the target,
            # search the left half of the array
            elif nums[mid] > target:
                high = mid - 1
            # If the middle element is less than the target,
            # search the right half of the array
            else:
                low = mid + 1

        # If the loop completes without finding the target, return -1
        return -1

        """
        Explanation of the approach:

        1. Binary Search Algorithm:
           - This implementation uses an iterative approach to binary search.
           - It repeatedly divides the search interval in half.

        2. Search Boundaries:
           - 'low' and 'high' represent the current search range in the array.
           - Initially set to the start and end of the array, respectively.

        3. Middle Element Calculation:
           - The middle index is calculated as (low + high) // 2.
           - Integer division ensures we get a valid array index.

        4. Comparison and Narrowing Search:
           - We compare the middle element with the target.
           - Based on this comparison, we eliminate half of the remaining elements:
             a. If the middle element is the target, we return its index.
             b. If the target is smaller, we search the left half (high = mid - 1).
             c. If the target is larger, we search the right half (low = mid + 1).

        5. Loop Termination:
           - The loop continues as long as low <= high.
           - If low becomes greater than high, it means the target is not in the array.

        6. Efficiency:
           - This algorithm is highly efficient for sorted arrays.
           - It reduces the search space by half in each iteration.

        7. Error Handling:
           - If the target is not found, the function returns -1.

        This implementation showcases the classic binary search algorithm,
        which is fundamental in computer science for its efficiency in searching sorted data.
        """
'''