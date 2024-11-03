/*
Given a random array arr of numbers, please return them in ascending sorted order.

Examples:

Input: arr[] = [1, 5, 3, 2]
Output: [1, 2, 3, 5]
Explanation: After sorting array will be like [1, 2, 3, 5].
Input: arr[] = [3, 1]
Output: [1, 3]
Explanation: After sorting array will be like [1, 3].
Constraints:
1 ≤ arr.size, arr[i] ≤ 105
*/


// User function Template for Java
class Solution {
    void sortArr(int[] arr) {
        // code here
        ArrayList<Integer> a=new ArrayList<Integer>();
        for(int i:arr)
        {
            a.add(i);
        }
        Collections.sort(a);
        for(int i=0;i<arr.length;i++)
        {
            arr[i]=a.get(i);
        }
    }
}
