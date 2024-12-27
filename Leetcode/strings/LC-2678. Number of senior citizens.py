class Solution:
    def countSeniors(self, details: List[str]) -> int: # type:ignore
        """
        Count the number of seniors (age > 60) in a list of personal details.

        This function efficiently counts seniors by iterating through the list once,
        extracting the age from each string, and comparing it directly as a string.

        Args:
        details (List[str]): A list of strings where each string contains personal details.
                             The age is assumed to be at indices 11 and 12 of each string.

        Returns:
        int: The number of seniors (people with age > 60) in the list.

        Time complexity: O(n), where n is the number of strings in the details list.
        Space complexity: O(1), as it uses only a constant amount of extra space.
        """
        cnt = 0
        for person in details:
            # Extract age directly as string and compare
            if person[11:13] > '60':
                cnt += 1
        return cnt

    # Alternative implementation using integer conversion
    # def countSeniors(self, details: List[str]) -> int:
    #     cnt = 0
    #     for person in details:
    #         age = int(person[11:13])
    #         if age > 60:
    #             cnt += 1
    #     return cnt

'''

## Explanation of the Optimized Approach

1. We initialize a counter `cnt` to 0.
2. We iterate through each string in the `details` list.
3. For each person's details:
   - We extract the age as a string using slicing (`person[11:13]`).
   - We compare this string directly with '60'.
   - If the age string is greater than '60', we increment the counter.
4. After processing all strings, we return the final count.

## Key Points

- **String Comparison**: By comparing the age as a string ('61', '62', etc.) directly with '60', we avoid the need for integer conversion. This works because string comparison in Python compares lexicographically, which aligns with numerical order for two-digit numbers.

- **Single Pass**: The algorithm makes a single pass through the list, ensuring O(n) time complexity.

- **Constant Space**: Only a single counter variable is used, resulting in O(1) space complexity.

## Asymptotic Analysis

- **Time Complexity**: O(n)
  - The function iterates through the list once, performing constant-time operations for each element.

- **Space Complexity**: O(1)
  - Uses only a constant amount of extra space (the `cnt` variable) regardless of input size.

This implementation is optimal for the given problem, balancing simplicity, efficiency, and readability.
'''