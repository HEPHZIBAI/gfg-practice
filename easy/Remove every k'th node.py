'''
Given a singly linked list, your task is to remove every kth node from the linked list. 

Examples:

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
Output: 1 -> 3 -> 5 -> 7

Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 -> 7.
Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10

Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.
Expected Time Complexity:  O(n)
Expected Auxiliary Space:  O(1)

Constraints:
1 <= size of linked list <= 106
1 <= node->data <= 106
1 <= k <= size of linked list

'''

#Your task is to complete this function
#Your function should return the new head pointer
'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
    
        if k==1:
            return 
        x=head
        n=1
        while(head.next):
            t=head
            while(n%k!=0 and head.next):
                t=head
                head=head.next
                n+=1
            if n%k==0:
                t.next=head.next
            else:
                break
            if head.next:
                head=head.next
                n+=1
        return x
        