#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    scanf("%d", &n);
    int l[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", l + i);
    }
    sort(l, l + n);
    int middle_i = n / 2;
    int middle = l[middle_i];
    long long tot = 0;
    for (int i = 0; i < middle_i; i++) {
        tot -= l[i];
    }
    for(int i = middle_i+1; i < n; i++){
        tot += l[i];
    }
    tot += middle * (middle_i+middle_i-n+1);
    printf("%lld", tot);

    return 0;
}