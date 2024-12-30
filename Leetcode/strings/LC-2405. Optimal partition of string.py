class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        substr = ''
        for char in s:
            if char in substr:
                count += 1
                substr = char
            else:
                substr += char
        return count + 1

'''
## Problem Explanation

LeetCode 2405: Optimal Partition of String

Given a string `s`, we need to partition it into one or more substrings such that the characters in each substring are unique. The goal is to find the minimum number of substrings in such a partition.

For example:
- Input: s = "abacaba"
- Output: 4
- Explanation: We can partition it into "ab", "ac", "ab", "a".

## Solution Approach

We use a greedy approach:
1. Iterate through the string.
2. Keep adding characters to the current substring until we encounter a repeat.
3. When a repeat is found, we close the current substring and start a new one.
4. Count the number of substrings formed.

## Edge Cases

1. Single character string: Returns 1.
2. String with all unique characters: Returns 1.
3. String with all repeated characters: Returns the length of the string.

## Asymptotic Analysis

- Time Complexity: O(n), where n is the length of the string.
  - We iterate through each character once.
  - The `in` operation on `substr` is O(1) on average, as it contains at most 26 characters.

- Space Complexity: O(1)
  - We use a fixed amount of extra space (`substr`) which is at most 26 characters long.

This solution efficiently solves the problem in a single pass through the string, using minimal extra space.
'''