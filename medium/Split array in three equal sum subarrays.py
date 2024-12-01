'''

Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If possible, return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.

Note: Since multiple answers are possible, return any of them. The driver code will print true if it is correct otherwise, it will print false.

Examples :

Input:  arr[] = [1, 3, 4, 0, 4]
Output: true
Explanation: [1, 2] is valid pair as sum of subarray arr[0..1] is equal to sum of subarray arr[2..3] and also to sum of subarray arr[4..4]. The sum is 4, so driver code prints true.
Input: arr[] = [2, 3, 4]
Output: false
Explanation: No three subarrays exist which have equal sum.
Input: arr[] = [0, 1, 1]
Output: false
Constraints:
3 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106

'''

class Solution:
    
    def findSplit(self, arr):
        total_sum = sum(arr)
        
        if total_sum % 3 != 0:
            return [-1, -1]

        target = total_sum // 3
        n = len(arr)
        current_sum = 0
        i = -1
        j = -1
    
        for index in range(n):
            current_sum += arr[index]
            if current_sum == target:
                i = index
                break
    
        if i == -1:
            return [-1, -1]
    
        current_sum = 0
        
        for index in range(i + 1, n):
            current_sum += arr[index]
            if current_sum == target:
                j = index
                break
    
        if j == -1 or sum(arr[j + 1:]) != target:
            return [-1, -1]
    
        return [i, j]