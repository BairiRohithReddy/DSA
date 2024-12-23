class Solution:
    def majorityElement(self, nums: List[int]) -> int: #type:ignore
        """
        Find the majority element in the given list of numbers.

        The majority element is the element that appears more than ⌊n / 2⌋ times,
        where n is the length of the list.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The majority element in the list.

        Note:
            This implementation assumes that the majority element always exists in the array.

        Time Complexity:
            O(n), where n is the length of nums. We iterate through the list twice:
            once to build the hashmap and once to find the majority element.

        Space Complexity:
            O(n) in the worst case, where all elements are unique and we store each in the hashmap.
            In the best case (all elements are the same), it would be O(1).
        """
        # Calculate the threshold for majority
        majority = len(nums) / 2

        # Create a hashmap to store the count of each number
        hashmap = {}

        # Count the occurrences of each number
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1  # Increment count if number already in hashmap
            else:
                hashmap[i] = 1   # Initialize count to 1 if it's a new number

        # Check if any number's count exceeds the majority threshold
        for i in nums:
            if hashmap[i] > majority:
                return i  # Return the first number that exceeds the majority threshold

        # Note: The problem assumes a majority element always exists,
        # so this line should never be reached
        return None


'''
The same problem can be solved using bayer-moore voting algorithm which only takes O(1) space complexity and O(n) time complexity.
'''