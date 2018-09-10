#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

long minimum(long x, long y){
    return (x<y)? x : y;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);


    long n;
    scanf("%ld", &n);
    long max_dig = (int)log2(n) + 1;

    long long tot = 0;
    long x;
    long mul = 1; // equal to 2^(i-1)
    for(int i = 1; i <= max_dig; i++, mul*=2){
        x = (n+mul)/mul/2;
        tot += mul*(x-1)+1 + minimum((n-mul)%(mul*2), mul-1);
    }
    printf("%lld", tot);
    return 0;
}