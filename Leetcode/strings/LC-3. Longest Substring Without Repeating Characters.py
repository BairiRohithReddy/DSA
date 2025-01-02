class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        This problem is solved using three different approaches, each with its own
        trade-offs in terms of time and space complexity.

        Args:
        s (str): The input string

        Returns:
        int: The length of the longest substring without repeating characters

        Approach 1: Naive String Manipulation
        ------------------------------------
        Idea:
        - Use a temporary string to store the current substring without repeats.
        - Iterate through the string, adding characters to the temp string.
        - If a duplicate is found, reset the temp string from after the first occurrence of the duplicate.

        Time Complexity: O(n^2), where n is the length of the string.
        - The outer loop iterates n times.
        - String operations (index and slicing) can take up to O(n) time.

        Space Complexity: O(min(m, n)), where m is the size of the character set.
        - The temp string stores at most min(m, n) characters.

        Pros: Simple to understand and implement.
        Cons: Inefficient for large strings due to quadratic time complexity.

        # max_length = 0
        # temp = ''
        # for i in range(len(s)):
        #     if s[i] not in temp:
        #         temp += s[i]
        #         max_length = max(len(temp), max_length) 
        #     else:
        #         temp = temp[temp.index(s[i])+1: ]
        #         temp += s[i]
        #         max_length = max(len(temp), max_length)
        # return max_length

        Approach 2: Optimized String Manipulation
        -----------------------------------------
        Idea:
        - Similar to Approach 1, but with slight optimizations.
        - Use a for-each loop instead of indexing.
        - Simplify the logic for updating max_length.

        Time Complexity: O(n^2), where n is the length of the string.
        - Despite optimizations, worst-case remains quadratic due to string operations.

        Space Complexity: O(min(m, n)), where m is the size of the character set.

        Pros: Slightly more concise than Approach 1.
        Cons: Still inefficient for large strings.

        # max_length = 0
        # temp = ''
        # for char in s:
        #     if char in temp:
        #         temp = temp[temp.index(char)+1: ]
        #     temp += char
        #     max_length = max(max_length, len(temp))
        # return max_length

        Approach 3: Sliding Window with Hash Map
        ----------------------------------------
        Idea:
        - Use a sliding window technique with two pointers (left and right).
        - Utilize a hash map to store the most recent index of each character.
        - When a duplicate is found, move the left pointer to the right of the previous occurrence.

        Time Complexity: O(n), where n is the length of the string.
        - Single pass through the string.
        - Hash map operations (insertion and lookup) are O(1) on average.

        Space Complexity: O(min(m, n)), where m is the size of the character set.
        - The hash map stores at most min(m, n) characters.

        Pros: Optimal time complexity, efficient for all input sizes.
        Cons: Slightly more complex to understand compared to naive approaches.
        """
        char_map = {}
        left = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            else:
                max_length = max(max_length, i - left + 1)
            char_map[char] = i
        return max_length
