'''
You are given an array of integers, your task is to divide the array into two sub-arrays (left and right) containing half of the array elements. Find the sum of the subarrays and then return the multiply of both the subarrays.

Note: If the length of the array is odd then the right half will contain one element more than the left half.

Examples :

Input : arr = [1, 2, 3, 4]
Output : 21
Explanation: Sum up an array from index 0 to 1 = 3, Sum up an array from index 2 to 3 = 7. Their multiplication is 21.
Input : arr = [1, 2] 
Output :  2 
Explanation: Their multiplication is 1*2 is equal to 2.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ arr.size() ≤ 1000
1 ≤ arr[i] ≤ 100

'''



class Solution:
    def multiply(self, arr):
        k=len(arr)//2
        
        a=arr[:k]
        b=arr[k:]
        
        return sum(a)*sum(b)