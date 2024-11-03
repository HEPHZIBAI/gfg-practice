'''
Given an array arr, return the second largest element from an array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the first largest.

Examples:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist..
Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
'''


#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        sl=-1
        l=max(arr)
        for i in arr:
            if i < l and i>sl:
                sl=i
        return sl