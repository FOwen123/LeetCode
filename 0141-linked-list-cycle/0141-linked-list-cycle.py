# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Two Pointers Method (Floyd's Cycle-Finding Algorithm/Hare and Tortoise Algorithm)
        
        # two pointers that move at different speeds. If there is a cycle, the fast pointer will eventually catch up to the slow pointer


        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        return False
            

        