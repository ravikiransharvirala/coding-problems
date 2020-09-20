'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


temp = 
cur.next = prev
prev = cur


prev = 1
cur =  cur.next

1st iter:

head = cur = 1
prev = None

temp = 2
cur.next = prev (prev = None)
prev = 1
cur = 2

2nd 
temp = 3
cur.next = 



'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev =  cur
                cur = temp
            head = prev
            return head
        else:
            return None



