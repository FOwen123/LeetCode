# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # This solution is to make the start of the head the same

        c1 = c2 = 0
        curr1, curr2 = headA, headB

        # Find the length of each linked list
        while curr1 or curr2:
            if curr1:
                c1 += 1
                curr1 = curr1.next
            
            if curr2:
                c2 += 1
                curr2 = curr2.next
            
        # Change the head so it has the same length
        c = c1 - c2
        while c != 0:
            if c < 0:
                headB = headB.next
                c += 1
            else:
                headA = headA.next
                c -= 1
        
        # Checking the head
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return headA