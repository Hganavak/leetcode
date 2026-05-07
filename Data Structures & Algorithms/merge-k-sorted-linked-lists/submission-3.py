# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    frequencyMap = {}

    # Create a frequency (hash) map
    for linkedListHead in lists:
      curr = linkedListHead

      while curr:
        frequencyMap.setdefault(curr.val, []).append(curr)
        curr = curr.next

    # Now link them
    dummy = ListNode()
    tail = dummy
    for key, nodes in sorted(frequencyMap.items()):
        for node in nodes:
            tail.next = node
            node.next = None
            tail = tail.next

    return dummy.next







