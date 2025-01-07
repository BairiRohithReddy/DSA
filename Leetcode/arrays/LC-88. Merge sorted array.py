class Solution:
    '''
        Merges two sorted arrays, nums1 and nums2, into a single sorted array in-place. 
        The first m elements of nums1 are the elements to be merged, and nums2 contains n elements.
        Approach 1:
        - Concatenate the first m elements of nums1 with all elements of nums2.
        - Sort the resulting array.
        - Asymptotic Analysis: This approach has a time complexity of O((m+n)log(m+n)) due to the sorting step.
        Approach 2:
        - Use three pointers to merge the arrays from the end to the beginning.
        - p1 points to the end of the valid elements in nums1.
        - p2 points to the end of nums2.
        - p points to the end of nums1.
        - Compare elements from nums1 and nums2 and place the larger one at the end of nums1.
        - Decrement the pointers accordingly.
        - Asymptotic Analysis: This approach has a time complexity of O(m+n) and a space complexity of O(1) since it modifies nums1 in-place.
        Args:
            nums1 (List[int]): The first sorted array with a size of m + n, where the first m elements are valid.
            m (int): The number of valid elements in nums1.
            nums2 (List[int]): The second sorted array with n elements.
            n (int): The number of elements in nums2.
        Returns:
            None: The function modifies nums1 in-place.
        '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: #type: ignore
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Approach 1: Concatenation and Sorting (commented out)
        # nums1[:] = nums1[:m] + nums2
        # nums1.sort()

        # Approach 2: Three-pointer in-place merge
        p1 = m - 1  # Pointer for the end of the valid portion of nums1
        p2 = n - 1  # Pointer for the end of nums2
        p = m + n - 1  # Pointer for the end of nums1 (including placeholder space)

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # If the current element in nums1 is larger, place it at the end
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # If the current element in nums2 is larger (or equal), or if we've exhausted nums1,
                # place the element from nums2 at the end
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Note: We don't need to handle any remaining elements in nums1,
        # as they are already in their correct positions.