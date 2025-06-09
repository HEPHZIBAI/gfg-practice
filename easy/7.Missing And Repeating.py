'''
Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].

Examples:

Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and smallest positive missing number is 1.
Input: arr[] = [1, 3, 3] 
Output: [3, 2]
Explanation: Repeating number is 3 and smallest positive missing number is 2.
Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5.
Constraints:
2 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()


'''

class Solution:
    def findTwoElement( self,arr): 
        n = len(arr)
    
        S = n * (n + 1) // 2
        S2 = n * (n + 1) * (2 * n + 1) // 6

        sum_arr = sum(arr)
        sum2_arr = sum(x * x for x in arr)

        diff1 = sum_arr - S         # y - x
        diff2 = sum2_arr - S2       # y^2 - x^2 = (y - x)(y + x)

        sum_xy = diff2 // diff1     # y + x
    
        y = (diff1 + sum_xy) // 2
        x = y - diff1

        return [y, x]
