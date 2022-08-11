# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = head
        while copy != None:
            while copy.next and copy.val == copy.next.val:
                copy.next = copy.next.next
            copy = copy.next
        return head