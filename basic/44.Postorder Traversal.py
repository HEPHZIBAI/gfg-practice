'''
Given a binary tree, find the Postorder Traversal of it and return a list containing the postorder traversal of the given tree.

Examples:

Input: root = [19, 10, 8, 11, 13]
        19
     /     \
    10      8
  /    \
 11    13
Output: [11, 13, 10, 8, 19]
Input: root = [11, 15, N, 7]
          11
         /
       15
      /
     7
Output: [7, 15, 11]
Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 106

'''


#User function Template for python3


'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        ans=[]
        def dfs(node):
            if not node:
                return
             
            dfs(node.left)
            dfs(node.right)
            
            ans.append(node.data)
         
        dfs(root)   
        return ans