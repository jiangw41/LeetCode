'''
LC2 Adding two numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        recursion version
        time O(max(D(l1), D(l2))) 95%; space recursion stack 32%
        '''
        if not l1 and not l2: return
        elif not l1: 
            if l2.val<10:
                return l2
            else: return ListNode(l2.val%10, Solution.addTwoNumbers(self, l2.next, ListNode(1, None)))
        elif not l2: 
            if l1.val<10: return l1
            else: return ListNode(l1.val%10, Solution.addTwoNumbers(self, l1.next, ListNode(1, None)))
        elif l1.val + l2.val >= 10: 
            if l1.next:
                l1.next.val+=1
                return ListNode((l1.val + l2.val)%10, Solution.addTwoNumbers(self, l1.next, l2.next))
            elif l2.next: 
                l2.next.val+=1
                return ListNode((l1.val + l2.val)%10, Solution.addTwoNumbers(self, l1.next, l2.next))
            else: 
                x = ListNode(1, None)
                return ListNode((l1.val + l2.val)%10, Solution.addTwoNumbers(self, x, None))
        else: return ListNode(l1.val + l2.val, Solution.addTwoNumbers(self, l1.next, l2.next))
#be careful of return values
        
    '''
    iteration version
    time O(max(D(l1), D(l2))) 11%; space O(1) 91%
    
    if (not l1) and (not l2): return None
        carry = 0  
        result = None
        while l1 or l2 or carry:
            if l1 and l2:
                val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + carry
                l1 = l1.next
            elif l2:
                val = l2.val + carry
                l2 = l2.next
            else: val = carry
            if val >= 10:
                val -= 10
                carry = 1
            else: carry = 0
            
            if not result: 
                result = ListNode(val, None)
                tem = result
                continue
            tem.next = ListNode(val, None)
            tem = tem.next
        return result
    '''
        

                    
            
            