class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        """
        Find the maximum number of words in any sentence from a list of sentences.

        Args:
        sentences (List[str]): A list of strings, each representing a sentence.

        Returns:
        int: The maximum number of words found in any sentence.

        Approach 1 (Nested Loop):
        - Iterate through each sentence and count spaces manually.
        - Time Complexity: O(n*m), where n is the number of sentences and m is the length of the longest sentence.
        - Space Complexity: O(1)
        - Issues: Fails to count single-word sentences correctly. Returns 1 for an empty list.

        Approach 2 (Using string.count()):
        - Use the count() method to count spaces in each sentence.
        - Time Complexity: O(n*m)
        - Space Complexity: O(1)
        - Issues: Same as Approach 1, fails for single-word sentences and empty lists.

        Approach 3 (Using string.split()):
        - Use split() to count words in each sentence.
        - Time Complexity: O(n*m)
        - Space Complexity: O(1) for the result, but O(m) temporary space for split()
        - Handles all cases correctly, including single-word sentences and empty lists.
        """

        # Approach 1: Nested Loop (Commented out)
        # max_count = 0
        # for i in range(len(sentences)):
        #     count = 0
        #     for j in range(len(sentences[i])-1):
        #         if sentences[i][j] == ' ':
        #             count += 1
        #     max_count = max(max_count, count)
        # if max_count > 0:
        #     max_count += 1
        # return max_count
       
        # Approach 2: Using string.count() (Commented out)
        # max_count = 0
        # for i in range(len(sentences)):
        #     count = sentences[i].count(" ")
        #     max_count = max(max_count, count)
        # if max_count >0:
        #     max_count += 1
        # return max_count

        # Approach 3: Using string.split()
        max_count = 0
        for sentence in sentences:
            count = len(sentence.split())
            max_count = max(max_count, count)
        return max_count

'''
Key points about each approach:
Approach 1 (Nested Loop):
1. Manually counts spaces in each sentence.
2. Issues: Fails to count words in sentences without spaces (single-word sentences).
3. Incorrectly returns 1 for an empty list due to the if max_count > 0 check.
Approach 2 (Using string.count()):
1. Uses the built-in count() method to count spaces.
2. Issues: Same problems as Approach 1 - doesn't handle single-word sentences or empty lists correctly.
Approach 3 (Using string.split()):
1. Uses split() to accurately count words, including single-word sentences.
2. Correctly handles all cases, including empty lists and single-word sentences.
3. Most efficient and accurate among the three approaches.
The final approach (Approach 3) resolves the issues you identified:
1. It correctly counts words in sentences without spaces.
2. It returns 0 for an empty list of sentences.
3. It accurately handles all valid input cases.
'''