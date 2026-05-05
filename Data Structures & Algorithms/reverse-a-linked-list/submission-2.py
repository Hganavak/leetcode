# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Edge cases
        if not head or not head.next:
            return head
        
        tmp=head
        queue=[]

        # Stack of values
        while tmp:
            print(f"{tmp.val=}")
            queue.append(tmp.val)

            tmp = tmp.next

        queue.reverse()
        print(f"{queue=}")

        # Turn this queue into a linked list
        new_head=ListNode(queue[0])
        curr = new_head

        for el in queue[1:]:
            curr.next = ListNode(el)
            curr = curr.next

        return new_head







