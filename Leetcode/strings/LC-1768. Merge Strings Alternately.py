class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately, character by character.

        Args:
        word1 (str): The first input string.
        word2 (str): The second input string.

        Returns:
        str: A new string with characters from word1 and word2 merged alternately.

        Approach 1 (Initial Implementation):
        - Use conditional statements to handle different length scenarios.
        - Iterate through the shorter word, appending characters alternately.
        - Append remaining characters from the longer word.
        
        Time Complexity: O(n), where n is the length of the longer word.
        Space Complexity: O(n) for the result string.
        
        Pros: Straightforward logic.
        Cons: Multiple conditional blocks, less efficient string concatenation.

        Approach 2 (Optimized Implementation):
        - Use a list to store merged characters.
        - Iterate up to the length of the longer word.
        - Append characters from each word if available.
        - Join the list to form the final string.

        Time Complexity: O(n), where n is the length of the longer word.
        Space Complexity: O(n) for the merged list and final string.

        Pros: More concise, efficient for appending, handles all cases in a single loop.
        Cons: Slightly higher memory usage due to list creation.

        Note: Both approaches have the same asymptotic complexity, but
        Approach 2 is generally more efficient in practice due to better
        use of Python's built-in operations.
        """
        # Approach 1 (Commented out)
        # result = ""
        # if len(word1) < len(word2):
        #     for i in range(len(word1)):
        #         result += word1[i] + word2[i]
        #     result += word2[i+1:]
        # elif len(word2) < len(word1):
        #     for i in range(len(word2)):
        #         result += word1[i] + word2[i]
        #     result += word1[i+1:]
        # else:
        #     for i in range(len(word1)):
        #         result += word1[i] + word2[i]
        # return result

        # Approach 2 (Implemented)
        merged = []  # List to store merged characters
        max_length = max(len(word1), len(word2))  # Length of the longer word

        for i in range(max_length):
            if i < len(word1):
                merged.append(word1[i])  # Append character from word1 if available
            if i < len(word2):
                merged.append(word2[i])  # Append character from word2 if available

        return ''.join(merged)  # Convert list to string
