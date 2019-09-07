public class reverse_linked_list {

    public static void main(String[] args){
        ListNode head = new ListNode(2);
        head.next = new ListNode(3);
        head.next.next = new ListNode(2);
        reverseList(head);
    }


    private static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        ListNode temp = prev;
        while (temp != null){
            System.out.println(temp.val);
            temp = temp.next;
        }

        return prev;
    }
}
