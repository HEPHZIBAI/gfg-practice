'''
Given an array arr[] of integers, calculate the median.
NOTE: Return the floor value of the median

Examples:

Input: arr[] = [90, 100, 78, 89, 67]
Output: 89
Explanation: After sorting the array middle element is the median 
Input: arr[] = [56, 67, 30, 79]
Output: 61
Explanation: In case of even number of elements, average of two middle elements is the median. 
Input: arr[] = [1,2]
Output: 1
Explanation: The average of both elements will result in 1.
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105
'''

#User function Template for python3

class Solution:
    def find_median(self, v):
        # Code here
        v.sort()
        l=len(v)//2
        if len(v)%2!=0:
            return v[l]
        else:
            return (v[l]+v[l-1])//2
