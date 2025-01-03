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
