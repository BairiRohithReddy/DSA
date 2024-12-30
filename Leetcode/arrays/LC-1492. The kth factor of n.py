class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Finds the kth factor of n using a single pass approach.

        This method iterates through numbers from 1 to n, counting factors
        and returning the kth factor when found.

        Args:
            n (int): The number to find factors for (1 <= n <= 1000).
            k (int): The position of the factor to return (1 <= k <= n).

        Returns:
            int: The kth factor of n, or -1 if n has less than k factors.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        # If k is greater than the number of factors, return -1
        return -1

    def approach2(self, n: int, k: int) -> int:
        """
        Finds the kth factor of n using a list to store factors.

        This method stores all factors in a list and returns the kth element
        if it exists.

        Args:
            n (int): The number to find factors for (1 <= n <= 1000).
            k (int): The position of the factor to return (1 <= k <= n).

        Returns:
            int: The kth factor of n, or -1 if n has less than k factors.

        Time Complexity: O(n)
        Space Complexity: O(sqrt(n)) average case, O(n) worst case
        """
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
            if len(result) >= k:
                return result[k - 1]
        # If k is greater than the number of factors, return -1
        return -1

'''
## Explanation of Edge Cases

Both methods handle the following edge cases:

1. **k greater than number of factors**: Both methods return -1 if n has fewer than k factors.
2. **n = 1**: Works correctly, returning 1 for k = 1 and -1 for k > 1.
3. **k = 1**: Always returns 1, as 1 is a factor of all positive integers.
4. **n = k**: Returns n if n is prime, -1 otherwise.

## Asymptotic Analysis

### kthFactor method:
- **Time Complexity**: O(n)
  - Iterates through numbers from 1 to n in the worst case.
- **Space Complexity**: O(1)
  - Uses only a constant amount of extra space.

### approach2 method:
- **Time Complexity**: O(n)
  - Iterates through numbers from 1 to n in the worst case.
- **Space Complexity**: 
  - Average case: O(sqrt(n)), as a number typically has about sqrt(n) factors.
  - Worst case: O(n), for numbers like n = 2^x, which have n/2 + 1 factors.

## Comparison of Approaches

1. **kthFactor**:
   - Pros: Constant space complexity, stops as soon as kth factor is found.
   - Cons: Cannot quickly access factors beyond the kth.

2. **approach2**:
   - Pros: Stores all factors, allowing quick access to any factor after computation.
   - Cons: Higher space complexity, always computes all factors even if k is small.

'''