//** Denis Piazentin **//
#include <stdio.h>
#define supersize 19
#define biglargenumber 1000000000LL

long long superlong[supersize];
int superIndex;
long long excess;
int i;
int maxI;
long long tmp;

void printsuperlong() {
	printf("%lld", superlong[maxI]);
	superlong[maxI] = 0;
	for (i = maxI - 1; i >= 0; i--) {
		printf("%09lld", superlong[i]);
		superlong[i] = 0;
	}
	printf("\n");
}

void multiply(int n) {
	excess = i = 0;
	do {
		tmp          = (superlong[i] * n) + excess;
		superlong[i] = tmp % biglargenumber;
		excess       = tmp / biglargenumber;
		
		i++;
		if ((maxI < i) && (excess != 0)) {
			maxI++;
		}

	} while(i < supersize && i <= maxI);
}

int main() {
    int t, n;    
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        superlong[0] = n;
        superIndex   = 0;
        maxI = 0;
        for(n = n - 1; n > 0; n--) multiply(n);
        printsuperlong();
    }
    return 0;
}
