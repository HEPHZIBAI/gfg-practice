/*
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: -1
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
1 <= arr.size <= 105
1 <= arr[i] <= 105
*/


class Solution {
    public int[] minAnd2ndMin(int arr[]) {
        HashSet<Integer> a=new HashSet<Integer>();
        int[] ans=new int[3];
        
        for(int i:arr)
            a.add(i);
        if (a.size()==1)
        {
            ans[0]=-1;
        }
        else
        {
            int s=100000;
            int ss=100000;
            for(int i:a)
            {
                if(i<s)
                {
                    ss=s;
                    s=i;
                }
                else if(i<ss)
                    ss=i;
            }
            ans[0]=s;
            ans[1]=ss;
        }
        return ans;
}}