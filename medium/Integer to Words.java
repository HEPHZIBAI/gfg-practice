/*

Write a function to convert a given number n into words.

The idea is to break down the number into International Number System, i.e., smaller groups of three digits (hundreds, tens, and ones), and convert each group into words.

Examples :

Input: n = 0
Output: "Zero"
Input: n = 123
Output: "One Hundred Twenty Three"
Input: n = 10245
Output: "Ten Thousand Two Hundred Forty Five"
Input: n = 2147483647
Output: "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
Constraints:
0 <= n <= 231-1

*/

class Solution 
{
    private static final String[] BELOW_20 = 
    {
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    };
    private static final String[] TENS = 
    {
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    };
    private static final String[] THOUSANDS = 
    {
        "", "Thousand", "Million", "Billion"
    };
    String convertToWords(int n) 
    {
        if (n == 0)
            return "Zero";

        String result = "";
        int group = 0;

        while (n > 0) 
        {
            if (n % 1000 != 0) 
                result = helper(n % 1000) + THOUSANDS[group] + " " + result;
    
            n /= 1000;
            group++;
        }

        return result.trim();
    }
    private static String helper(int num) {
        if (num == 0) {
            return "";
        } else if (num < 20) {
            return BELOW_20[num] + " ";
        } else if (num < 100) {
            return TENS[num / 10] + " " + helper(num % 10);
        } else {
            return BELOW_20[num / 100] + " Hundred " + helper(num % 100);
        }
    }
}