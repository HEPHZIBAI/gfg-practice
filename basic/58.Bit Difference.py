'''
You are given two numbers a and b. The task is to count the number of bits needed to be flipped to convert a to b.

Examples:

Input: a = 10, b = 20
Output: 4
Explanation:
a  = 01010
b  = 10100
As we can see, the bits of A that need to be flipped are 01010. If we flip these bits, we get 10100, which is B.
Input: a = 20, b = 25
Output: 3
Explanation:
a  = 10100
b  = 11001
As we can see, the bits of A that need to be flipped are 10100. If we flip these bits, we get 11001, which is B.
Constraints: 
1 ≤ a, b ≤ 106
'''




class Solution:
    def countBitsFlip(self, a, b):
        xor_result = a ^ b
        count = 0
        
        while xor_result:
            count += xor_result & 1
            xor_result >>= 1
        
        return count