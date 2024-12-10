class Solution:
    """
    A class to solve the 'Contains Duplicate' problem.
    
    This class provides multiple approaches to determine if a given list of integers
    contains any duplicate elements.
    """

    def containsDuplicate(self, nums: List[int]) -> bool: # type: ignore
        """
        Determines if the input list contains any duplicate elements.

        :param nums: A list of integers
        :return: True if the list contains duplicates, False otherwise
        """

        # Approach 1: Using a dictionary as a hash set
        # hashset = {}
        # for num in nums:
        #     if num in hashset:  # If number is already in hashset, it's a duplicate
        #         return True
        #     hashset[num] = 1  # Add number to hashset
        # return False  # No duplicates found

        # Approach 2: Using Counter
        # freq = Counter(nums)  # Count frequency of each number
        # for num, count in freq.items():
        #     if count >= 2:  # If any number appears 2 or more times, it's a duplicate
        #         return True
        # return False  # No duplicates found

        # Approach 3: Comparing lengths of list and set
        # return len(set(nums)) < len(nums)  # If set is smaller, there were duplicates

        # Approach 4: Using a set as a hash set
        hashset = set()  # Initialize an empty set
        for num in nums:
            if num in hashset:  # If number is already in set, it's a duplicate
                return True
            hashset.add(num)  # Add number to set
        return False  # No duplicates found