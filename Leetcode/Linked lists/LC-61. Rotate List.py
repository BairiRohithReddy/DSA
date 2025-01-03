# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: #type:ignore
        """
        Rotates the given linked list to the right by k places.
        Args:
            head (Optional[ListNode]): The head of the linked list.
            k (int): The number of places to rotate the list.
        Returns:
            Optional[ListNode]: The new head of the rotated linked list.
        Detailed Explanation:
        1. If the list is empty, has only one node, or k is 0, return the head as no rotation is needed.
        2. Calculate the length of the linked list.
        3. Compute the effective rotation steps needed by taking k modulo length.
        4. If the effective rotation steps are 0, return the head as no rotation is needed.
        5. Traverse the list to find the new tail (length - k - 1) and the new head (length - k).
        6. Adjust the pointers to rotate the list:
           - Set the next of the new tail to None.
           - Set the next of the old tail to the old head.
        7. Return the new head of the rotated list.
        Asymptotic Analysis:
        - Time Complexity: O(N), where N is the number of nodes in the linked list. This is because we traverse the list twice: once to calculate the length and once to find the new tail.
        - Space Complexity: O(1), as we are using a constant amount of extra space.
        Edge Cases:
        - The list is empty (head is None).
        - The list has only one node.
        - k is 0 or a multiple of the length of the list.
        Example:
        Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 2,
        the rotated list will be 4 -> 5 -> 1 -> 2 -> 3.
        Inline Comments:
        - Check if the list is empty, has only one node, or k is 0.
        - Initialize the length of the list to 1 and set the current node to head.
        - Traverse the list to calculate its length.
        - Compute the effective rotation steps needed.
        - If no rotation is needed, return the head.
        - Traverse the list to find the new tail.
        - Set the new head and adjust the pointers to rotate the list.
        - Return the new head.
        """
        if not head or not head.next or k ==0:
            return head 
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        k = k % length
        if k ==0:
            return head
        temp = head
        for _ in range(length-k-1):
            temp = temp.next
        new_head = temp.next
        curr.next = head
        temp.next = None
        return new_head
'''
for _ in range(length - k - 1): This loop moves temp to the node just before the new head. 
The underscore _ is used as a variable name when the variable's value is not needed.
length - k - 1: This calculates the position of the node just before the new head. 
For example, if the list length is 5 and k is 2, the new head should be at position 3 (0-based index), so temp should stop at position 2
'''