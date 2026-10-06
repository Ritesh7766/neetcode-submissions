# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        trev = head
        while trev:
            if trev in visited:
                return True
            visited.add(trev)
            trev = trev.next
        return False
