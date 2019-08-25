class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(self, head):
        
        current = head
        while current!=None and current.next!=None:
            if current.val==current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head