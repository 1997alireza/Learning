#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    long long x;
    scanf("%lld", &x);
    printf("%lld ", x);
    while(x != 1){
        if(x % 2 == 0) x /= 2;
        else x = x*3 + 1;
        printf("%lld ", x);
    }
    return 0;
}