from collections import deque

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def addTwoNumbers(l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur =ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //=10
        return dummy.next






def addTwoNumbersineinefficient(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
  
        l1_list = deque([])
        l2_list = deque([])
        
        head = l1
        while head:
            l1_list.appendleft(head.val)
            head = head.next
        head = l2
        while head:
            l2_list.appendleft(head.val)
            head = head.next            
            
            
        total = str(int(''.join(str(e) for e in l1_list)) + int(''.join(str(e) for e in l2_list)))
        print(total)
        head = output = ListNode(total[len(total)-1])
        
        
        start = len(total)-2
        while start>=0:
            output.next = ListNode(total[start])
            output = output.next
            start-=1
        return head
        
test = ListNode(1)
test.next = ListNode(2)

test2 = ListNode(2)
test2.next = ListNode(1)

addTwoNumbers(test, test2)
addTwoNumbersineinefficient(test, test2)