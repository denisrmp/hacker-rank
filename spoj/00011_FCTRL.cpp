//** Denis Piazentin **//
#include <stdio.h>

int main() {
    long long t, n, five, zn, tmp;    
    scanf("%lld", &t);
    while(t--) {
        scanf("%lld", &n);
        zn = 0;
        for(five = 5; tmp = n/five; five*=5) zn += tmp;
        printf("%lld\n", zn);
    }
    return 0;
}
