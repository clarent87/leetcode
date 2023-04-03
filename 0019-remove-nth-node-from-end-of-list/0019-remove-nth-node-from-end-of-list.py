# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        end = head
        while end != None:
            count += 1
            end = end.next

        if count == n:
            head = head.next
            return head

        else:
            m = head
            for x in range(count -n -1):
                m = m.next

            if m.next != None:
                m.next = m.next.next

        return head