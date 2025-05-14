/*
Given a linked list. Print all the elements of the linked list separated by space followed.

Examples:

Input: LinkedList : 1 -> 2

Output: 1 2
Explanation: The linked list contains two elements 1 and 2.The elements are printed in a single line.
Input: Linked List : 49 -> 10 -> 30
 
Output: 49 10 30
Explanation: The linked list contains 3 elements 49, 10 and 30. The elements are printed in a single line.
Expected Time Complexity: O(n)
Expected Auxiliary Space : O(1)
 
Constraints :
1 <= numbers of nodes <= 105
1 <= node values <= 106
*/

class Solution {
    void display(Node head) {
        // add code here.
        while(head.next!=null)
        {
            System.out.print(head.data+" ");
            head=head.next;
        }
        System.out.print(head.data+" ");
    }
}