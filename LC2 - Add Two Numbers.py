# %%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# %%
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cursum = 0
        head = cur = ListNode(0)
        while l1 or l2 or carry > 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            cursum = x + y + carry
            if cursum > 9:
                cursum = cursum - 10
                carry = 1
            else:
                carry = 0
            cur.next = ListNode(cursum)
            cur = cur.next

            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
        return head.next


# %%
#Initialise linked lists
v1 = [9,9,9,9,9,9,9]
v1 = [2,4,3]
l1 = cur = ListNode(v1[0])
for v in v1[1:]:
    cur.next = ListNode(v)
    cur = cur.next

v2 = [9,9,9,9]
v2 = [5,6,4]
l2 = cur = ListNode(v2[0])
for v in v2[1:]:
    cur.next = ListNode(v)
    cur = cur.next

# %%
#Print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

    
# %%
s = Solution()
linked_list_str(s.addTwoNumbers(l1,l2))