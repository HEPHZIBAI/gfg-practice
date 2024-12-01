'''
Given a singly linked list containing nodes with English alphabets ('a'-'z'). Rearrange the linked list in such a way that all the vowels come before the consonants while maintaining the order of their arrival. 

Examples:

Input: Linked list: a -> b -> c -> d -> e -> f -> g -> h -> i 
Output: a -> e -> i -> b -> c -> d -> f -> g -> h

Explanation: After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.
Input: Linked list: a -> b -> a -> b -> d -> e -> e -> d 
Output: a -> a -> e -> e -> b -> b -> d -> d

Explanation: After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.
Expected Time Complexity :  O(n)
Expected Auxiliary Space :  O(1)

Constraints:
1 <= size of linked list <= 106
'a' <= elements of linked list <= 'z'
'''

#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        x=Linked_List()
        y=head
        while head:
            if head.data in "aeiou":
                x.insert(head.data)
            head=head.next
        head=y 
        while head:
            if head.data not in "aeiou":
                x.insert(head.data)
            head=head.next
            
        return x.head
