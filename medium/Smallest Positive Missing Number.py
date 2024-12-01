'''
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.
Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.
Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.
Constraints:  
1 <= arr.size() <= 105
-106 <= arr[i] <= 106
'''

class Solution:
    def missingNumber(self,arr):
        arr=list(set(arr))
        arr.sort()

        if arr[-1]<=0:
            return 1
        
        i=0
        
        while(i<len(arr) and arr[i]<=0):
            i+=1
        
        k=1
        while i<len(arr) and k==arr[i]:
            k+=1
            i+=1
        return k
