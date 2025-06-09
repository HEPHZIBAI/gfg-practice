'''
You are given an Integer n. Return true if It is a Leap Year otherwise return false.

Examples:

Input: n = 4
Output: true
Explanation: 4 is not divisible by 100 and is divisible by 4 so its a leap year
Input: n = 2021
Output: false
Explanation: 2021 is not divisible by 100 and is also not divisible by 4 so its not a leap year
Constraints:
1<= n < 104

'''



class Solution:
    def checkYear (self, n):
        return (n%4==0 and n%100!=0) or n%400==0