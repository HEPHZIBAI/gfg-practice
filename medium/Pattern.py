'''
Geek is very fond of patterns. Once, his teacher gave him a star pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a star pattern.

Example 1:


Example 2:



Your Task:

You don't need to input anything. Complete the function printDiamond() which takes an integer n  as the input parameter and prints the pattern.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:

1<= n <= 100
'''

#User function Template for python3

class Solution:
    def printDiamond(self, N):
        for i in range(N):
            for j in range(N-i-1):
                print("",end=" ")
            for l in range(0,i+1):
                print("*",end=" ")
            print()
        for i in range(N):
            for j in range(0,i):
                print("",end=" ")
            for l in range(N-i):
                print("*",end=" ")
            print()