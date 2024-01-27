# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0
        while l1 != None and l2 != None:
            res.val = l1.val + l2.val + carry
            if res.val > 9:
                res.val -= 10 
                carry = 1
            else:
                carry = 0
    
            res.next = ListNode()
            prev = res
            res = res.next
            l1 = l1.next
            l2 = l2.next
        if l1 != None:
            print("l1", l1.val, "carry", carry)
            while l1 != None:
                res.val = l1.val + carry
                if res.val > 9:
                    res.val -= 10 
                    carry = 1
                else:
                    carry = 0
                res.next = ListNode()
                prev = res
                res = res.next
                l1 = l1.next
        if l2 != None:
            print("l2", l2.val, "carry", carry)
            while l2 != None:
                res.val = l2.val + carry
                if res.val > 9:
                    res.val -= 10 
                    carry = 1
                else:
                    carry = 0
                res.next = ListNode()
                prev = res
                res = res.next
                l2 = l2.next
        res.val = res.val + carry
        if res.val == 0:
            prev.next = None
    
        return head