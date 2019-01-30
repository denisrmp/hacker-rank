#include <cstdio>
#include <cstdlib>

int main() {
    int t, i, times;
    long long a, m, r;
    char b[252];
    scanf("%d", &t);
    while (t-- > 0) {
        scanf("%lld %s %lld", &a, b, &m);
        i=0;
        r=1;
        a %= m;
        while(b[++i]!='\0'); 
        --i;
        while(i >= 0) { 
            for (times = 0; times < (b[i]-48); times++) {
                r *= a;
            }
            r %= m;
            a = (a*a*a) % m;
            i--;
        }
        printf("%d\n", (int) r);
    }
    return 0;
}
