'''

Given an array arr of integers and an index key(0-based index). Your task is to return the element present at the index key in the array.

Examples:

Input: key = 2 , arr = [10, 20, 30, 40, 50]
Output: 30
Explanation: The value of arr[2] is 30 .
Input: key = 4 , arr = [10, 20, 30, 40, 50, 60, 70]
Output: 50
Explanation: The value of the arr[4] is 50 .
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
0 ≤ key ≤ arr.size - 1
1 ≤ arr.size ≤ 106
1 ≤ arr[i] ≤ 109

'''

from typing import List


class Solution:
    def findElementAtIndex(self, key : int, arr : List[int]) -> int:
        # code here
        return arr[key]