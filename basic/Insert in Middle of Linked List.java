/*
Given the head of a Singly Linked List and a value x. The task is to insert the key in the middle of the linked list.

Examples :

Input: LinkedList = 1->2->4 , x = 3
Output: 1->2->3->4
Explanation: 

The new element is inserted after the current middle element in the linked list.
Input: LinkedList = 10->20->40->50 , x = 30
Output: 10->20->30->40->50
Explanation: 

The new element is inserted after the current middle element in the linked list and Hence, the output is 10->20->30->40->50.
Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
0 <= number of nodes <= 105
0 <= node->data , x <= 103
*/

class Solution {
    public Node insertInMiddle(Node head, int x) {
        // Code here
        
            
        Node a=new Node(x);
        if(head==null)
            return a;
        Node t=head;
        int s=0;
        while(t.next != null)
        {
            t=t.next;
            s++;
        }
        t=head;
        for(int i=0;i<s/2;i++)
        {
            t=t.next;
        }
        a.next=t.next;
        t.next=a;
        return head;
    }
}