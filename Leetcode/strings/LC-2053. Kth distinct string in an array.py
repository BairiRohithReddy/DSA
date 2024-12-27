class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str: #type: ignore
        """
        Find the kth distinct string in the array.

        This function efficiently finds the kth distinct string by using a hashmap
        to count occurrences and a list to store distinct elements.

        Args:
        arr (List[str]): An array of strings.
        k (int): The position of the distinct string to return (1-indexed).

        Returns:
        str: The kth distinct string, or an empty string if there are fewer than k distinct strings.

        Time complexity: O(n), where n is the length of arr.
        Space complexity: O(n) in the worst case, to store the count of each string and the list of distinct elements.
        """
        # Initialize hashmap with all elements set to count 0
        hashmap = {i: 0 for i in arr}
        res = []

        # Count occurrences of each string
        for i in arr:
            hashmap[i] += 1

        # Collect distinct elements (those with count 1)
        for i, count in hashmap.items():
            if count == 1:
                res.append(i)

        # Check if k is greater than the number of distinct elements
        if k > len(res):
            return ""

        # Return the kth distinct element (k is 1-indexed)
        return res[k-1]

'''
## Explanation of the Approach

1. **Initialization**: We create a hashmap with all elements from `arr` as keys, initially setting their count to 0.

2. **Counting Occurrences**: We iterate through `arr` once, incrementing the count for each element in the hashmap.

3. **Collecting Distinct Elements**: We iterate through the hashmap, appending elements with a count of 1 (distinct elements) to the `res` list.

4. **Handling Edge Case**: We check if `k` is greater than the number of distinct elements. If so, we return an empty string.

5. **Returning Result**: We return the `k-1`th element of `res` (subtracting 1 because `k` is 1-indexed but list indices are 0-indexed).

## Asymptotic Analysis

- **Time Complexity**: O(n)
  - We iterate through the input array twice: once to count occurrences and once to collect distinct elements.
  - Both operations are linear in the size of the input.

- **Space Complexity**: O(n)
  - In the worst case, the hashmap and `res` list could contain all elements of the input array.

This implementation efficiently solves the problem with a good balance of time and space complexity.
'''