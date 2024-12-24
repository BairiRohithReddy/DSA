class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: #type:ignore
        """
        Find all numbers from 1 to n that do not appear in the input list.

        Args:
            nums (List[int]): An array of integers where 1 ≤ a[i] ≤ n (n = size of array).

        Returns:
            List[int]: A list of all integers in the range [1, n] that do not appear in nums.
        """

        def approach1(nums: List[int]) -> List[int]:    #type:ignore
            """
            Approach 1: Brute Force

            Time Complexity: O(n^2)
            Space Complexity: O(n)

            Note: This approach may result in Time Limit Exceeded for large inputs.
            """
            n = len(nums)
            result = []
            for i in range(1, n+1):
                if i not in nums:
                    result.append(i)
            return result

        def approach2(nums: List[int]) -> List[int]:    #type:ignore
            """
            Approach 2: Using Set for Faster Lookup

            Time Complexity: O(n)
            Space Complexity: O(n)

            Note: This approach is more efficient than Approach 1 but still may be slow for very large inputs.
            """
            n = len(nums)
            num_set = set(nums)
            result = []
            for i in range(1, n+1):
                if i not in num_set:
                    result.append(i)
            return result

        def approach3(nums: List[int]) -> List[int]:    #type:ignore
            """
            Approach 3: Set Difference

            Time Complexity: O(n)
            Space Complexity: O(n)

            Note: This is the most concise and efficient approach among the four.
            """
            return list(set(range(1, len(nums)+1)) - set(nums))

        def approach4(nums: List[int]) -> List[int]:    #type:ignore
            """
            Approach 4: List Comprehension

            Time Complexity: O(n^2)
            Space Complexity: O(n)

            Note: This approach may result in Time Limit Exceeded for large inputs,
            similar to Approach 1, due to the 'not in' operation being O(n).
            """
            n = len(nums)
            return [i for i in range(1, n+1) if i not in nums]
        
        def approach5(nums: List[int]) -> List[int]:    #type:ignore
            # using hashset
            result = []
            nums_dict = {i:0 for i in range(1, len(nums))}
            for num in nums_dict:
                nums_dict[num] += 1
            for k, v in nums_dict.values():
                if v == 0:
                    result.append(v)
            return result                

        # Uncomment the approach you want to use
        # return approach1(nums)
        # return approach2(nums)
        return approach3(nums)
        # return approach4(nums)

'''
Approaches 1 and 2 differ significantly in their lookup efficiency due to the underlying data structures used:

## Approach 1: List

In the first approach, the 'in' operation is performed on a list. Lists in Python are implemented as dynamic arrays, which means:

- Checking if an element is in a list requires a linear search through the entire list.
- This results in an O(n) time complexity for each 'in' operation.
- With n such operations, the overall time complexity becomes O(n^2).

## Approach 2: Set

The second approach converts the list to a set before performing lookups. Sets in Python are implemented using hash tables, which provides:

- Near-constant time O(1) lookup operations on average.
- This significant speedup is due to the hash function used to compute the position of each element.
- Even with n lookups, the time complexity remains O(n).

## Why Sets Are Faster

Converting nums to a set leads to this decrease in time complexity because:

1. Sets use hash functions to determine if an element is present, avoiding the need to iterate through all elements[3].
2. Hash table lookups are typically O(1) operations, making them significantly faster for large datasets[2].
3. While creating the set initially takes O(n) time, subsequent lookups benefit from the constant-time average case complexity[1].

This efficiency difference is particularly noticeable with large datasets. For example, searching through 100,000 items takes 49.663 seconds with a list, but only 0.007 seconds with a set[2].

Resources:
[1] https://www.youtube.com/watch?v=xzDEEzH8XWk
[2] https://blog.enterprisedna.co/python-set-vs-list-the-real-difference/
[3] https://stackoverflow.com/questions/2831212/python-sets-vs-lists
[4] https://towardsdatascience.com/python-set-is-way-faster-than-list-true-or-false-042c6f8975cd
'''