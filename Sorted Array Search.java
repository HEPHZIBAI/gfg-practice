/*
Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

Examples:

Input: arr[] = [1, 2, 3, 4, 6], k = 6
Output: true
Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
Input: arr[] = [1, 2, 4, 5, 6], k = 3
Output: false
Exlpanation: Since, 3 is not present in the array, output is false.
Input: arr[] = [2, 3, 5, 6], k = 1
Output: false
Constraints:
1 <= arr.size() <= 106
1 <= k <= 106
1 <= arr[i] <= 106

*/




class Solution {
    static boolean searchInSorted(int arr[], int k) 
    {
        // Your code here
        int l=0;
        int r=arr.length-1;
        while(l<=r)
        {
            int mid=(l+r)/2;
            if(arr[mid]==k)
                return true;
            else if(arr[mid]>k)
                r=mid-1;
            else
                l=mid+1;
        }
        return false;
    }
}