class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Calculate the length of the last word in a string.

        LeetCode Problem 58: Length of Last Word

        A word is defined as a maximal substring consisting of non-space characters only.

        Args:
        s (str): A string containing words separated by spaces. The string may contain
                 leading or trailing spaces.

        Returns:
        int: The length of the last word in the string.

        Approach:
        1. Split the string into words using the split() method.
        2. Access the last word using index -1.
        3. Return the length of the last word.

        Time Complexity: O(n), where n is the length of the string.
        - split() method traverses the entire string once.
        - Accessing the last element and calculating its length are O(1) operations.

        Space Complexity: O(n)
        - In the worst case, split() creates a list of n/2 words (if every other character is a space).

        Note: This solution efficiently handles strings with multiple spaces between words
        and leading/trailing spaces, as split() without arguments splits on any whitespace.
        """
        words = s.split()  # Split the string into words
        result = len(words[-1])  # Get the length of the last word
        return result

# approach -2
# the above solution has O(n) time and space complexity which can be optimised for O(n) time complexity and O(1) space complexity
def lengthofLastWord(s: str) -> int:
    length = 0
    i = len(s) -1    
    # not counting trailing spaces
    while i>= 0 and s[i] == ' ':
        i -= 1   
    while i>=0 and s[i] != ' ':
        length += 1
        i -= 1
    return length

'''
Optimized Approach
Instead of using string splitting or creating additional data structures, we can use a single-pass, reverse iteration method:
Start from the end of the string.
Skip any trailing spaces.
Count non-space characters until we hit a space or the beginning of the string.
This approach is more efficient because:
It avoids creating any new data structures.
It only needs to traverse part of the string in most cases.
It handles trailing spaces without needing to trim the string first.
Complexity Analysis
Time Complexity: O(n) in the worst case, where n is the length of the string. However, it's often better in practice as it may not need to traverse the entire string.
Space Complexity: O(1), as it uses only a constant amount of extra space.
'''