# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodeMap = {}
        i = 1

        while curr:
            nodeMap[i] = curr

            i += 1
            curr = curr.next

        length = i - 1
        targetIndex = length - n + 1

        if targetIndex == 1: # We're cutting out the first element anyway
            if head:
                return head.next

        # If there is a previous node
        prevNode = nodeMap[targetIndex - 1] 
        prevNode.next = nodeMap.get(targetIndex + 1)

        return head
