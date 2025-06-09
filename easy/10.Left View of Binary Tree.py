'''
You are given the root of a binary tree. Your task is to return the left view of the binary tree. The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.

If the tree is empty, return an empty list.

Examples :

Input: root[] = [1, 2, 3, 4, 5, N, N]

Output: [1, 2, 4]
Explanation: From the left side of the tree, only the nodes 1, 2, and 4 are visible.

Input: root[] = [1, 2, 3, N, N, 4, N, N, 5, N, N]

Output: [1, 2, 4, 5]
Explanation: From the left side of the tree, the nodes 1, 2, 4, and 5 are visible.

Input: root[] = [N]
Output: []
Constraints:
0 <= number of nodes <= 106
0 <= node -> data <= 105

'''


#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

            # First node at this level
                if i == 0:
                    result.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result