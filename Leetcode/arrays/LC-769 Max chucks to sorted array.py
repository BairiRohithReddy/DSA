'''
## **Problem: Max Chunks To Make Sorted (LeetCode 769)**

### **Problem Statement**
You are given an array `arr` of integers (0-indexed) that is a permutation of `[0, 1, ..., arr.length - 1]`. You need to partition the array into *maximum chunks* such that after sorting each chunk individually and concatenating them back together, the resulting array is sorted in ascending order.

### **Example 1**
Input: `arr = [1, 2, 3, 4, 0]`  
Output: `1`  
Explanation: The entire array must be considered as one chunk because the element `0` is at the last index. Sorting any smaller chunks would not result in a sorted array.

### **Example 2**
Input: `arr = [0, 1, 2, 3, 4]`  
Output: `5`  
Explanation: Each element is already in its correct position. Therefore, we can form 5 chunks (one for each element).

---

## **Approach**

### **Key Insight**
The key observation is that in a sorted array `[0, 1, ..., n-1]`, each element's value matches its index. To form valid chunks:
- The maximum value in a chunk must equal the last index of that chunk.
- If this condition is satisfied at index `i`, it means all elements from the start of the chunk to index `i` are correctly positioned relative to each other.

### **Algorithm**
1. Initialize:
   - A variable `max_so_far` to track the maximum value seen so far in the array.
   - A counter `result` to count the number of chunks.
2. Iterate through the array using enumeration (`i` as index and `n` as value).
3. For each element:
   - Update `max_so_far` to be the maximum of itself and the current element (`n`).
   - If `max_so_far == i`, it means all elements up to index `i` can form a valid chunk. Increment `result`.
4. Return `result`.

---
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int: #type:ignore
        # Initialize variables
        max_so_far = -1  # Tracks the maximum value seen so far
        result = 0       # Counts the number of chunks
        
        # Iterate through each element in the array
        for i, n in enumerate(arr):
            # Update max_so_far with the maximum of current max_so_far and current element
            max_so_far = max(max_so_far, n)
            
            # If max_so_far equals the current index, we can form a chunk
            if max_so_far == i:
                result += 1
        
        # Return the total number of chunks
        return result

'''
## **Intuition Building**

To build a deeper understanding of this problem:

1. **Understand Chunk Formation**:
   - A chunk can only be formed when all elements within it are "sorted" relative to their positions in the final sorted array.
   - This happens when the maximum value encountered so far (`max_so_far`) equals the current index (`i`). At this point, all elements up to `i` are guaranteed to be in their correct positions relative to each other.

2. **Think About Sorted Arrays**:
   - In a sorted array like `[0, 1, 2, ..., n-1]`, every element matches its index. Hence, every single element can form its own chunk.
   - In an unsorted permutation like `[1, 2, 3, 4, 0]`, elements are misplaced such that only one large chunk can satisfy the condition for sorting.

3. **Visualize with Examples**:
   - Example: `[4, 3, 2, 1, 0]`
     - At every step, `max_so_far` keeps increasing but never matches the index until the very end. Hence only one chunk is possible.
   - Example: `[2, 0, 1]`
     - At index `2`, `max_so_far = 2`, which matches the index. This forms one valid chunk.

4. **Edge Cases**:
   - Single-element arrays like ``: Always result in one chunk.
   - Already sorted arrays like `[0, 1, ..., n-1]`: Result in as many chunks as there are elements.

---

## **Complexity Analysis**

- **Time Complexity**: $$O(n)$$, where $$n$$ is the length of the array.
   - We iterate through the array once to calculate `max_so_far`.
- **Space Complexity**: $$O(1)$$, as no additional data structures are used.

---

## **Why This Approach Works**

This approach leverages a fundamental property of permutations and sorting:
- The maximum value encountered so far (`max_so_far`) acts as a boundary for forming chunks.
- When `max_so_far == i`, it guarantees that all elements up to index `i` are correctly positioned relative to each other.

By breaking down this property into simple checks during iteration, we efficiently determine where chunks can be formed without explicitly sorting or manipulating subarrays.

---

'''