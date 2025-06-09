'''
Given an array arr of even size, the task is to find a minimum value that can be added to an element so that the array becomes balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of the right half.

Examples :

Input: arr = [1, 5, 3, 2]
Output: 1
Explanation: Sum of first 2 elements is 1 + 5  = 6, Sum of last 2 elements is 3 + 2  = 5, To make the array balanced you can add 1.
Input: arr = [1, 2, 1, 2, 1, 3]
Output: 2
Explanation: Sum of first 3 elements is 1 + 2 + 1 = 4, Sum of last three elements is 2 + 1 + 3 = 6, To make the array balanced you can add 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2<=arr.size()<=107 where arr.size() is even.
1<=arr[i]<=105

'''


class Solution:
    def min_value_to_balance(self, arr):
        l=len(arr)//2
        a=arr[:l]
        b=arr[l:]
        
        return abs(sum(a)-sum(b))