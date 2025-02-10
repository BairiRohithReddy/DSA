# Definition for singly-linked list.
"""
This module contains the implementation of a singly-linked list node and a solution to add two numbers represented by two linked lists.
Classes:
    ListNode: A class representing a node in a singly-linked list.
    Solution: A class containing a method to add two numbers represented by linked lists.
Methods:
    Solution.addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Adds two numbers represented by two linked lists and returns the sum as a linked list.
        Parameters:
            l1 (Optional[ListNode]): The head of the first linked list.
            l2 (Optional[ListNode]): The head of the second linked list.
        Returns:
            Optional[ListNode]: The head of the resulting linked list representing the sum of the two numbers.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: #type:ignore
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            new_val = v1 + v2 + carry
            carry = new_val // 10
            new_val = new_val % 10
            curr.next = ListNode(new_val)
            
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummy.next