'''

Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list and return the head of the updated list.

Examples:

Input: LinkedList: 2<->4<->5, p = 2, x = 6 
Output: 2<->4<->5<->6
Explanation: p = 2, and x = 6. So, 6 is inserted after p, i.e, at position 2 (0-based indexing).
Input: LinkedList: 1<->2<->3<->4, p = 0, x = 44
Output: 1<->44<->2<->3<->4
Explanation: p = 0, and x = 44 . So, 44 is inserted after p, i.e, at position 0 (0-based indexing).
Constraints:
0 <= p < size of doubly linked list <= 106
1 <= x <= 106

'''



# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        nn=Node(x)
        k=0
        a=head
        b=head.next
        
        while k<p and a and b:
            #print(a.data,end=" ")
            a=a.next
            b=a.next
            k+=1
        #print(a.data)
            
        if not b:
            a.next=nn
            nn.prev=a
        else:
            a.next=nn
            nn.prev=a
            nn.next=b
            b.prev=nn

        '''if a:
            print("a",a.data)
        if b:
            print("b",b.data)'''
        
        return head