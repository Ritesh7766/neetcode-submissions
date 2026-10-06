# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        trev1 = headA
        while trev1:
            visited.add(trev1)
            trev1 = trev1.next
        
        trev2 = headB
        while trev2:
            if trev2 in visited:
                return trev2
            trev2 = trev2.next
        return None