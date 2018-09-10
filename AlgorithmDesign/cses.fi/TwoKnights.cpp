#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    scanf("%d", &n);
    long long ans = 0;
    for(int k = 1; k < 6 and k <= n; k++){
        switch (k) {
            case 1: ans = 0; break;
            case 2: ans = 6; break;
            case 3: ans = 28; break;
            case 4: ans = 96; break;
            case 5: ans = 252; break;
        }
        printf("%lld\n", ans);
    }
    for(long long k = 6; k <= n; k++){
        ans += 9*(k-1)*(k-1) - 24 + (2*k-10)*(k*k-2*k-3) + (2*k-1)*(k-1);
        printf("%lld\n", ans);
    }
    return 0;
}