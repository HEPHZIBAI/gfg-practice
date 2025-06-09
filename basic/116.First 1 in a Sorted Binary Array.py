'''
Given a sorted array arr consisting of 0s and 1s. The task is to find the index (0-based indexing) of the first 1 in the given array.

NOTE: If one is not present then, return -1.

Examples :

Input : arr[] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
Output : 6
Explanation: The index of first 1 in the array is 6.
Input : arr[] = [0, 0, 0, 0]
Output : -1
Explanation: 1's are not present in the array.
Expected Time Complexity: O(log (n))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 1



'''

class Solution:
    def firstIndex(self, arr):
        if 1 in arr:
            return arr.index(1)
        else:
            return -1

