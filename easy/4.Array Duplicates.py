'''
Given an array arr of integers, find all the elements that occur more than once in the array. Return the result in ascending order. If no element repeats, return an empty array.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.
Input: arr[] = [0, 3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty.
Input: arr[] = [2]
Output: [] 
Explanation: There is single element in the array. Therefore output is empty.
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 106
'''

from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        a=list(set(arr))
        a.sort()
        arr.sort()
        if a==arr:
            return [-1]
        else:
            a=[]
            for i in arr:
                if arr.count(i)>1:
                    a.append(i)
            return list(set(a))

