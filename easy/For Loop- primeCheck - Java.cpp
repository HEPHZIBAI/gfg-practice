/*
What do you do when you need to execute certain statements more than once? You put them in a loop. Loops are very powerful. The majority of coding questions need loops to work. You can't even input test cases without loops!

Here, we will use for loop and check if the given number n is prime or not.

Note:  A number is prime if it's divisible by itself and 1 only. Also, 1 is not prime.

Example 1:

Input:
n = 1
Output:
No
Example 2:

Input:
n = 2
Output:
Yes
Your Task:
You don't need to read input or print anything. Your task is to complete the function isPrime() which takes the integer n as a parameter and returns a string "Yes" or "No".

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
1 <= n <= 105
*/

// User function Template for C++

void isPrime(int n) 
{
    int f=1;
    for (int i = 2; i <= sqrt(n); i++) 
    {
        if(n%i==0)
        {
            f=0;
            break;
        }
    }
    if(n==1||f==0)
        cout<<"No";
    else
        cout<<"Yes";
    cout << endl;
}