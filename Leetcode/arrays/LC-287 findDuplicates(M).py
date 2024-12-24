class Solution:
    def findDuplicate(self, nums: List[int]) -> int: #type:ignore
        """
        Find the duplicate number in an array of integers.

        This problem can be solved using two different approaches:
        1. Using a HashSet (Set)
        2. Using Floyd's Cycle Detection Algorithm (Tortoise and Hare)

        Args:
            nums (List[int]): An array of integers containing n + 1 integers
                              where each integer is in the range [1, n] inclusive.

        Returns:
            int: The duplicate number in the array.
        """

        def approach_hashset(nums: List[int]) -> int: #type:ignore
            """
            Approach 1: Using a HashSet

            Time Complexity: O(n)
            Space Complexity: O(n)

            This approach uses extra space but is straightforward and efficient.
            """
            hashset = set()
            for num in nums:
                if num in hashset:
                    return num
                hashset.add(num)

        def approach_floyd_cycle(nums: List[int]) -> int: #type:ignore
            """
            Approach 2: Floyd's Cycle Detection (Tortoise and Hare)

            Time Complexity: O(n)
            Space Complexity: O(1)

            This approach uses constant extra space and is optimal for this problem.
            """
            # Phase 1: Detect cycle
            slow = fast = nums[0]
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break

            # Phase 2: Find entrance to the cycle
            slow = nums[0]
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            
            return slow

        # Choose which approach to use
        # return approach_hashset(nums)
        return approach_floyd_cycle(nums)
