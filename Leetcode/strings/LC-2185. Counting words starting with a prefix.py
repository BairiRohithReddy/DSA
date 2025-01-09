class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int: #type:ignore
        """
        Count the number of words in the list that start with the given prefix.
        This function iterates through the list of words and checks if each word starts with the given prefix.
        It uses slicing to compare the prefix with the beginning of each word.
        Args:
            words (List[str]): A list of words to be checked.
            pref (str): The prefix to be matched.
        Returns:
            int: The count of words that start with the given prefix.
        Approach:
            1. Initialize a counter `cnt` to 0.
            2. Iterate through each word in the list.
            3. For each word, check if the substring from the start to the length of the prefix matches the prefix.
            4. If it matches, increment the counter.
            5. Return the counter.
        Asymptotic Analysis:
            - Time Complexity: O(n * m), where n is the number of words and m is the length of the prefix.
              This is because for each word, we are comparing up to m characters.
            - Space Complexity: O(1), as we are using a constant amount of extra space.
        Alternative Approach (Commented Out):
            - The commented-out approach uses the `startswith` method to check if each word starts with the prefix.
            - This approach also has a time complexity of O(n * m) and a space complexity of O(1).
        """
        # cnt = 0
        # for i in words:
        #     if i.startswith(pref):
        #         cnt += 1
        # return cnt

        cnt = 0
        i, j = 0, len(pref)

        for k in range(len(words)):
            if words[k][i:j] == pref:
                cnt += 1
        return cnt

        #  return sum([for word in words if word.startswith(pref)])
