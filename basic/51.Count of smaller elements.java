/*
Given an unsorted array arr. Find the count of elements less than or equal to the given element x.

Examples:

Input: x = 9, arr = [10, 1, 2, 8, 4, 5] 
Output: 5
Explanation: The 5 elements are 1, 2, 8, 4 and 5.
Input: x = 2, arr = [1, 2, 2, 5, 7, 2, 9] 
Output: 4 
Explanation: The 4 elements are 1, 2, 2 and 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 105
1 <= ai <= 105
0 <= x <= 105
*/



class Solution{
    public int countOfElements(int []arr,int n,int x)
    {
        int s=0;
        for(int i:arr)
        {
            if(i<=x)
                s+=1;
        }
        return s;
    }
}