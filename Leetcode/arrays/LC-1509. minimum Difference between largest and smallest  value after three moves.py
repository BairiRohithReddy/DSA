# class Solution:
#     def minDifference(self, nums: List[int]) -> int: #type:ignore
#         # checking for edge casess where len of array is 4 or less than 4
#         if len(nums) < 5:
#             return 0
        
#         # now moving on to cases where there are more than 4 elements in the array
#         # first we sort the given nums
#         # then we can change upto 3 values
#         # so inorder to get min difference, we have to change either from starting or from the last
#         # so in case 1 we change all three values from the left
#         # now the result is nums[-4] - nums[0]
#         # now we change one from the start and 2 from the end
#         # now the result will be nums[-3] - nums[1]
#         # we then change 2 from the start and 1 from the end
#         # result = nums[-2] - nums[2]
#         # then  from the start
#         # result = nums[-1] - nums[3]
        
#         return min(nums[-4]- nums[0], nums[-3]-nums[1], nums[-2]-nums[2], nums[-1]-nums[3])
    
class Solution:
    def approach1(self, nums: List[int]) -> int:
        """
        Approach 1: Direct Comparison After Sorting

        Idea:
        - Sort the array
        - Compare the differences between the 4 smallest and 4 largest elements
        - Return the minimum difference

        Asymptotic Analysis:
        - Time Complexity: O(n log n)
          * Sorting takes O(n log n)
          * Subsequent operations are constant time O(1)
        - Space Complexity: O(1)
          * Sorting is done in-place
          * Only a constant number of variables are used

        where n is the length of the input array nums
        """
        if len(nums) < 5:
            return 0
        
        nums.sort()  # O(n log n)
        
        # O(1) operation
        return min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1] - nums[3])

    def approach2(self, nums: List[int]) -> int:
        """
        Approach 2: Using zip() for Pairwise Comparison

        Idea:
        - Sort the array
        - Use zip() to pair the 4 smallest with the 4 largest elements
        - Calculate differences and return the minimum

        Asymptotic Analysis:
        - Time Complexity: O(n log n)
          * Sorting takes O(n log n)
          * zip() and min() operations are O(1) as they operate on fixed-size lists
        - Space Complexity: O(1)
          * Sorting is in-place
          * zip() creates a fixed-size iterator
        """
        if len(nums) <= 4:
            return 0
        
        nums.sort()  # O(n log n)
        
        # O(1) operation as it's always processing 4 pairs
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))

    def approach3(self, nums: List[int]) -> int:
        """
        Approach 3: Explicit Comparisons in Reverse Order

        Idea:
        - Sort the array
        - Explicitly calculate differences, starting from largest gap
        - Return the minimum difference

        Asymptotic Analysis:
        - Time Complexity: O(n log n)
          * Sorting takes O(n log n)
          * Subsequent operations are constant time O(1)
        - Space Complexity: O(1)
          * Sorting is in-place
          * Only uses a constant amount of extra space
        """
        if len(nums) <= 4:
            return 0
        
        nums.sort()  # O(n log n)
        
        # O(1) operation
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])

    def approach4(self, nums: List[int]) -> int:
        """
        Approach 4: Separate Sorting for Min and Max

        Idea:
        - Separately sort and select the 4 smallest and 4 largest elements
        - Use zip() to pair and calculate differences
        - Return the minimum difference

        Asymptotic Analysis:
        - Time Complexity: O(n log n)
          * Sorting the entire array takes O(n log n)
          * Selecting 4 elements is O(1)
          * zip() and min() on 4 pairs is O(1)
        - Space Complexity: O(1)
          * Only stores 8 elements (4 min and 4 max)
        """
        if len(nums) <= 4:
            return 0
        
        # O(n log n) for sorting
        min_nums = sorted(nums)[:4]  # O(1) for slicing
        max_nums = sorted(nums)[-4:]  # O(1) for slicing
        
        # O(1) operation as it's always processing 4 pairs
        return min(b - a for a, b in zip(min_nums, max_nums))

    def approach5(self, nums: List[int]) -> int:
        """
        Approach 5: Using max() and min() on Slices

        Idea:
        - Sort the array
        - Use slicing with max() and min() to consider all change scenarios
        - Return the minimum difference

        Asymptotic Analysis:
        - Time Complexity: O(n log n)
          * Sorting takes O(n log n)
          * Subsequent max(), min() operations on slices are O(n)
          * Overall complexity is dominated by sorting: O(n log n)
        - Space Complexity: O(1)
          * Sorting is in-place
          * Slicing creates views, not copies
        """
        if len(nums) <= 4:
            return 0
        
        nums.sort()  # O(n log n)
        
        # Each max() and min() operation is O(n), but there are only 4 pairs
        return min(max(nums[:-3]) - min(nums[3:]),
                   max(nums[:-2]) - min(nums[2:]),
                   max(nums[:-1]) - min(nums[1:]),
                   max(nums) - min(nums[:-3]))
