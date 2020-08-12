# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        bin_val = ''
        while node:
            bin_val += str(node.val)
            node = node.next
        res = int(bin_val,2)
        return res


lNode = ListNode(1)
lNode.next = ListNode(0)
lNode.next.next = ListNode(1)
s = Solution()
print(s.getDecimalValue(lNode))

lNode2 = ListNode(0)
s = Solution()
print(s.getDecimalValue(lNode2))

lNode3 = ListNode(1)
s = Solution()
print(s.getDecimalValue(lNode3))

lNode4 = ListNode(1)
lNode4.next = ListNode(0)
lNode4.next.next = ListNode(0)
lNode4.next.next.next = ListNode(1)
lNode4.next.next.next.next = ListNode(0)
lNode4.next.next.next.next.next = ListNode(0)
lNode4.next.next.next.next.next.next = ListNode(1)
lNode4.next.next.next.next.next.next.next = ListNode(1)
lNode4.next.next.next.next.next.next.next.next = ListNode(1)
lNode4.next.next.next.next.next.next.next.next.next = ListNode(0)
lNode4.next.next.next.next.next.next.next.next.next.next = ListNode(0)
lNode4.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
lNode4.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
lNode4.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
lNode4.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
s = Solution()
print(s.getDecimalValue(lNode4))
        