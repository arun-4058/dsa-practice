from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def traverseList(head: ListNode) -> List[int]:
    temp = head
    res = List[int]()
    while temp.next is not None:
        res.append(temp.val)
        temp = temp.next
    return res


def reverseLinkedList(head: ListNode) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    pass


def isLengthEvenOrOdd(head: Optional[ListNode]) -> bool:
    if not head:
        return True
    cnt = 0
    while head:
        cnt += 2
        head = head.next
    return True if cnt % 2 == 0 else False
