class Solution:
    def partitionLabels(self, s: str) -> List[int]: #type:ignore
        # Store the last occurrence index of each character in the string
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []          # List to store partition lengths
        size = 0          # Current partition size
        end = 0           # End index of current partition
        
        # Iterate through string to find partitions
        for i, c in enumerate(s):
            size += 1     # Increment current partition size
            
            # Update the end index by taking maximum of current end
            # and last occurrence of current character
            end = max(end, lastIndex[c])
            
            # If current index equals end index, we've found a partition
            if i == end:
                res.append(size)    # Add partition size to result
                size = 0           # Reset size for next partition
        
        return res

"""
Time Complexity: O(n) 
- First loop through string to create lastIndex map: O(n)
- Second loop through string to create partitions: O(n)
- Total: O(n) where n is length of input string

Space Complexity: O(1)
- lastIndex hashmap stores at most 26 characters (lowercase English letters)
- Result list varies but is bounded by input length
- Since input alphabet is fixed, space is constant O(1)
"""
