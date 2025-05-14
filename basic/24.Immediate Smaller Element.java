/*

Given an integer array arr. For each element in the array, check whether the right adjacent element (on the next immediate position) of the array is smaller. If next element is smaller, update the current index to that element. If not, then update to -1. Return the modified array.

Examples:

Input: arr[] = [4, 2, 1, 5, 3]
Output: [2, 1, -1, 3, -1]
Explanation: Array elements are 4, 2, 1, 5, 3. Next to 4 is 2 which is smaller, so we print 2. Next of 2 is 1 which is smaller,so we print 1. Next of 1 is 5 which is greater, so we print -1. Next of 5 is 3 which is smaller, so we print 3.  Note that for last element, output is always  going to be -1 because there is no element on right.
Input: arr[] = [5, 6, 2, 3, 1, 7]
Output: [-1, 2, -1, 1, -1, -1]
Explanation: Next to 5 is 6 which is greater, so we print -1. Next of 6 is 2 which is smaller, so we print 2. Next of 2 is 3 which is greater, so we print -1. Next of 3 is 1 which is smaller, so we print 1. Next of 1 is 7 which is greater, so we print -1. Note that for last element, output is always going to be -1 because there is no element on right.
Input: arr[] = [4, 1]
Output: [1, -1]
Explanation: 4 will be updated to 1 and 1 will be updated to -1.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105



*/



//User function Template for Java

class Solution {
    void immediateSmaller(int arr[], int n) {
        // code here
        for(int i=0;i<arr.length-1;i++)
        {
            if(arr[i]>arr[i+1])
                arr[i]=arr[i+1];
            else
                arr[i]=-1;
        }
        arr[n-1]=-1;
    }
}