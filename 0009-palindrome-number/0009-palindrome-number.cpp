class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0)    return false;

        int n=x;
        long int rev=0;
        while (n > 0) {
            rev = (rev*10)+(n%10);
            n /= 10;
        }

        // if (x==rev)
        //     return true;
        // return false;
        return (x==rev);

    } 
};