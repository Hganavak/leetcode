# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:

    if not head or not head.next: return

    # Step 1: Find the mid-point (fast and slow pointer)
    slow = head
    fast = head.next

    while slow.next and fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    print(f"{slow.val=}")

    # Step 2: Reverse all the links in the second linked list
    second = slow.next
    slow.next = None  # cut the list

    prev = None
    curr = second

    while curr:
      tmp = curr.next
      curr.next = prev

      prev = curr
      curr = tmp
      
    # Now we move second to prev (the last place we got to in our loop)
    second = prev

    if second:
      print(f"{second.val=}")

    # Step 3: Swaperoo
    first = head

    if not first or not second:
      return

    while second:
      assert first # Pylance being annoying

      firstTmp = first.next
      secondTmp = second.next

      first.next = second
      second.next = firstTmp

      first = firstTmp
      second = secondTmp
