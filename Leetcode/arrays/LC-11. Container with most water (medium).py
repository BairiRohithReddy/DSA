class Solution:
    def maxArea(self, height: List[int]) -> int: #type:ignore
        """
        Calculate the maximum area of water that can be contained between two vertical lines.

        Args:
            height (List[int]): A list of integers where each integer represents the height of a vertical line.

        Returns:
            int: The maximum area of water that can be contained.

        Time Complexity: O(n), where n is the length of the height list.
        Space Complexity: O(1), as we only use a constant amount of extra space.
        """

        """
        CAUTION: The following approach is incorrect for this problem and is left here for educational purposes.
        This approach does not solve the Container With Most Water problem but might be applicable to a different problem.

        def incorrect_approach(height: List[int]) -> int:
            prev_vol = 0
            next_vol = 0
            for i in range(1, len(height)-1):
                current = height[i]
                prev_vol = max(prev_vol, height[i] - height[i-1])
                next_vol = max(prev_vol, height[i] - height[i+1])
            return max(prev_vol, next_vol)

        Note: This approach incorrectly calculates the difference between adjacent heights
        instead of the area between two lines. It does not solve the Container With Most Water problem.
        """

        # Edge case: if there are only two lines, return the area between them
        if len(height) == 2:
            return min(height)
        
        left = 0
        right = len(height) - 1
        curr_max = 0

        # Two-pointer approach to find the maximum area
        while left < right:
            # Calculate the current area and update max if necessary
            curr_max = max(curr_max, min(height[left], height[right]) * (right - left))
            
            # Move the pointer pointing to the shorter line inward so we can maximize the area between the two lines
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return curr_max