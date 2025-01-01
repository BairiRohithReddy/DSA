class Solution:
    def maxScore(self, s: str) -> int:
        """
        Calculate the maximum score after splitting a string.

        The score is calculated as the number of zeros in the left substring
        plus the number of ones in the right substring.

        Args:
        s (str): A string consisting of only '0' and '1' characters.

        Returns:
        int: The maximum possible score.

        Approach 1 (Brute Force):
        - Iterate through all possible split points.
        - For each split, count zeros in left part and ones in right part.
        - Keep track of the maximum score.

        Time Complexity: O(n^2), where n is the length of the string.
        Space Complexity: O(1).

        Approach 2 (Optimized):
        - Pre-count total ones in the string.
        - Iterate once through the string, updating zero and one counts.
        - Dynamically calculate and update the maximum score.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(1).

        Author's Note:
        The initial approach involved a nested loop structure, recounting ones 
        in each iteration. This led to redundant calculations and O(n^2) time complexity.
        The optimized solution pre-counts ones and updates counts in a single pass,
        significantly improving efficiency to O(n) time complexity.
        """

        # Approach 1: Brute Force (Commented out)
        # zeros = 0
        # ones = 0
        # max_score = 0
        #
        # for i in range(0, len(s)-1):
        #     if s[i] == "0":
        #         zeros += 1
        #     for j in range(i+1, len(s)-1):
        #         ones = s[i+1:].count("1")
        #         max_score = max(max_score, zeros + ones)
        #
        # return max_score

        # Approach 2: Optimized Solution
        zeros = 0
        ones = s.count("1")  # Pre-count total ones in the string
        max_score = 0

        # Iterate through the string, updating counts and max score
        for i in range(len(s) - 1):  # Exclude the last character
            if s[i] == "0":
                zeros += 1  # Increment zeros count for left substring
            else:
                ones -= 1   # Decrement ones count for right substring
            max_score = max(max_score, zeros + ones)  # Update max score
        
        return max_score
