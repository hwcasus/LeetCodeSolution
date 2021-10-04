# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not all(lists):
            lists = [l for l in lists if l]

        if not lists:
            return None

        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(self.mergeTwoLists(l1, l2))

        return lists[0]


    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ret = head = ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                head.next = head = l2
                l2 = l2.next
            else:
                head.next = head = l1
                l1 = l1.next

        head.next = l1 or l2
        return ret.next


    def mergeKListsFirst(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not all(lists):
            lists = [l for l in lists if l]

        if not lists:
            return None

        ret = head = ListNode(0)

        while lists:
            idx, _ = min(enumerate(lists), key=lambda idx_node: idx_node[1].val)
            head.next = head = lists[idx]
            lists[idx] = lists[idx].next
            if not lists[idx]:
                lists.pop(idx)

        return ret.next