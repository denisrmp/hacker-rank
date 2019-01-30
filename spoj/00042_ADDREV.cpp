#include <stdio.h>

int main() {
    int n;
    long a, b, reversedA, reversedB, reversedSum, sum;

    scanf("%d", &n);
    while(n--) {
        scanf("%ld %ld", &a, &b);
        reversedA = reversedB = 0;
        while (a || b) {
            if (a) {
                reversedA = (reversedA * 10) + (a % 10);
                a /= 10;
            }

            if (b) { 
                reversedB = (reversedB * 10) + (b % 10);
                b /= 10;
            }
        }
        sum = 0;
        reversedSum = reversedA + reversedB;
        while (reversedSum) {
            sum = (sum * 10) + (reversedSum % 10);
            reversedSum /= 10;
        }

        printf("%ld\n", sum);
    }

    return 0;
}
