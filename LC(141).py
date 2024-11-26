# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
# approach 1 O(n) complexity
        # currentElement = head
        # present = set()
        # while currentElement:
        #     if currentElement in present:
        #         return True
        #     present.add(currentElement)
        #     currentElement = currentElement.next
        # return False

#second approach optimising for O(1) we can use slow pointer and fast pointer approach
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False