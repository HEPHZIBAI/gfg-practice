'''
Given a list of names, display the longest name. If there are multiple names of the longest size, return the first occurring name.

Examples :

Input: names[]= ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]
Output: GeeksforGeeks
Explanation: name "GeeksforGeeks" has maximum length among all names. 
Input: names[]=["Apple", "Mango", "Orange", "Banana"]
Output: Orange
Explanation: names "Orange" and "Banana" both have maximum length among all names but Orange comes first so answer will be "Orange". 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= names.size()<= 1000
1 <= size(names[i]) <= 1000
names[i] has only lowercase and uppercase letters
'''

class Solution:
    def longest(self, names):
        # code here
        l=0
        k=""
        for i in names:
            if len(i)>l:
                l=len(i)
                k=i
        return k
