/*
You are given an integer array arr[]. The task is to find the sum of it.

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size <= 105
1 <= arr[i] <= 104
*/



// User function Template for Java

class Solution {
    int sum(int arr[], int n) {
        int s=0;
        for(int i:arr)
            s+=i;
        return s;
    }
}