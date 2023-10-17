# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pointer1=head #initializing pointer1

        pointer2=head   #initializing pointer2 which will move 2x fast as pointer2

        while pointer2 is not None and pointer2.next is not None:   
            #while pointer2 is not none and while the next element of it is not none
            pointer1=pointer1.next  #pointer 1 moves up by 1
            pointer2=pointer2.next.next #pointer 2 moves up twice

        return pointer1 #return pointer1, since pointer 1 moves 2x less, when pointer2 reaches end, pointer1 will still be at middle of linkedlist
        