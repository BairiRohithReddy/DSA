# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: #type:ignore
        def list_to_num(node):
            num = 0
            multiplier = 1
            while node:
                num += node.val * multiplier
                multiplier *= 10
                node = node.next
            return num
        
        def num_to_list(num):
            dummy = ListNode(0) #type:ignore
            current = dummy
            if num == 0:
                return dummy.next
            while num != 0:
                digit = num % 10
                current.next = ListNode(digit) #type:ignore
                current = current.next
                num //= 10
            return dummy.next
        
        num1 = list_to_num(l1)
        num2 = list_to_num(l2)
        total = num1 + num2
        return num_to_list(total)
