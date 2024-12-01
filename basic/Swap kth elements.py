'''
Given an array arr, swap the kth element from the beginning with the kth element from the end.

Note: 1-based indexing is followed.

Examples :

Input: k = 3, arr = [1, 2, 3, 4, 5, 6, 7, 8]
Output: [1, 2, 6, 4, 5, 3, 7, 8]
Explanation: 3rd element from beginning is 3 and 3rd element from end is 6, so we replace 3 & 6.
Input: k = 2, arr = [5, 3, 6, 1, 2]
Output: [5, 1, 6, 3, 2]
Explanation: 2nd element from beginning is 3 and from end is 1.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ k ≤ arr.size() ≤ 106
-109 ≤ arr[i] ≤ 109

'''

class Solution:
    def swapKth(self, k, arr):
        # Code Here
        arr[k-1],arr[k*-1]=arr[k*-1],arr[k-1]