class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int n = x;

        while (n > 0)
        {
            sum += n%10;
            n /= 10;
        }

        return x%sum ? -1: sum;
        // if (x%sum==0)
        //     return sum;
        // return -1;
    }
};