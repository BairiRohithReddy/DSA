'''
19. Remove Nth node from the end of a linked list

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
'''

#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def length(self):
    #     currentNode = head
    #     length=0
    #     while currentNode is not None:
    #         length+=1
    #         currentNode = currentNode.next
    #     return length

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length=0
        currentNode = head
        while currentNode is not None:
            length+=1
            currentNode = currentNode.next
        position = length-n
        currentPosition = 0
        currentNode = dummy
        while currentNode is not None:
            if currentPosition == position:
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next
            currentPosition+=1
        return dummy.next              
