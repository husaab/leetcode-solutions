# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head #initialize fast
        slow = head #initialize slow

        while fast is not None and fast.next is not None:   #while fast is not none and fast.next is not none
            fast = fast.next.next       #fast is equal to fast.next.next
            slow = slow.next            #slow is equal to slow.next
            if slow == fast:            #if they eventually meet, then that means there is a cycle
                return True     #so, return true

        return False        #else, return false
        