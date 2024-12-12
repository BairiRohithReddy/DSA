class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # type:ignore
        """
        Find the longest common prefix string amongst an array of strings.

        Args:
        strs (List[str]): An array of strings to search for a common prefix.

        Returns:
        str: The longest common prefix string. If there is no common prefix, return an empty string "".

        Time Complexity: O(S), where S is the sum of all characters in the array.
        Space Complexity: O(1), only using a constant amount of extra space.
        """
        
        # Check if the input list is empty
        if len(strs) == 0:
            return ""  # If empty, there's no common prefix, so return an empty string
        
        # Initialize the prefix as the first string in the list
        # This is our starting point, assuming the first string could be the common prefix
        prefix = strs[0]
        
        # Iterate through the remaining strings in the list, starting from the second string
        for i in range(1, len(strs)):
            # While the current string doesn't start with our prefix
            while strs[i][0: len(prefix)] != prefix:
                # Shorten the prefix by removing the last character
                # This is done because if the current prefix isn't found, a shorter version might be
                prefix = prefix[0: len(prefix) - 1]
                
                # If the prefix becomes empty, it means there's no common prefix
                if len(prefix) == 0:
                    return ""  # Return empty string as there's no common prefix
        
        # If we've made it through all strings without returning, 
        # the current prefix is the longest common prefix
        return prefix
    