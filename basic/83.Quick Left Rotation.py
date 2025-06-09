'''
Given an array, arr[] of positive elements, and an integer k, the task is to left-rotate the array k indexes.
Note: Rotate the array even if the k is greater than the size of the array. In these cases after every full array rotation, the array comes the same as the original array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5, 6, 7], k = 2 
Output: [3, 4, 5, 6, 7, 1, 2]
Explanation: Rotating the above array by 2 will make the output array.
Input: arr[] = [1, 2, 3, 4, 5, 6],  k = 12
Output: [1, 2, 3, 4, 5, 6]
Explanation: left Rotation of above array 12 times gives same array as output. 
Input: arr[] = [1, 2, 3, 4, 5, 6],  k = 11
Output: [6, 1, 2, 3, 4, 5]
Explanation: left Rotation of above array 11 times & in resultant output 6 comes to the statring position.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size, arr[i] ≤ 105
0 ≤ k ≤ 109


'''
class Solution:
    def leftRotate(self, arr, k):
        while len(arr)<=k:
            k%=len(arr)
            
        arr[::]=arr[k:]+arr[:k]

