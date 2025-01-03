# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: #type:ignore
        # Edge case: if the list is empty, return None
        if not head:
            return head

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # If current node's value is same as next node's value,
                # skip the next node by updating the next pointer
                curr.next = curr.next.next
            else:
                # If values are different, move to the next node
                curr = curr.next
        
        return head

# Approach 2 : Brute Force

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: #type:ignore
        # Edge case: if the list is empty, return None
        if not head:
            return head        
        while head is not None:
            curr = head
            while curr.next is not None:
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next            
        return head     

'''

## Intuition
The idea behind this approach is to iterate through the linked list once, comparing each node with its next node. If two adjacent nodes have the same value, we skip the next node by updating the current node's next pointer to the node after the next node.

## Asymptotic Analysis
- Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.
- Space Complexity: O(1), as we only use a constant amount of extra space regardless of the input size.

## Edge Cases
1. Empty list: Handled at the beginning of the function.
2. List with all duplicate elements: The algorithm will reduce it to a single node.
3. List with no duplicates: The algorithm will traverse the entire list without making changes.

## Potential Pitfalls
1. Memory management: In languages with manual memory management, care should be taken to properly free the memory of removed nodes.
2. Modifying the head: This implementation doesn't need a dummy node because it never modifies the head of the list. However, if the problem required removing the head in some cases, a dummy node would be necessary.

## Additional Notes
1. This algorithm maintains the original order of elements.
2. It works in-place, modifying the original list rather than creating a new one.
3. The algorithm assumes the input list is already sorted. If the list isn't sorted, this method won't remove all duplicates.

'''