/*

Given an array arr, print all its elements space-separated.

Note: You don't need to move to the next line after printing all elements of the array (space-separated)

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: 1 2 3 4 5
Input: arr[] = [2, 3, 5, 5]
Output: 2 3 5 5
Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
1 <= arr.size <= 106
1 <= arr[i] <= 108

*/


// User function Template for Java

class Solution {
    //Just print the space seperated array elements
    void printArray(int arr[], int n) {
        //   code here
        for(int i: arr)
            System.out.print(i+" ");
    }
}