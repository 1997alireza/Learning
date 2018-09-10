#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, max;
    scanf("%d%d", &n, &max);
    int w[n];
    for(int i = 0; i < n; i++) scanf("%d", w+i);
    sort(w, w+n);
    int start = 0, end = n-1;
    int res = 0;
    while(start <= end) {
        if (w[start] + w[end] <= max) {
            start++;
        }
        res++;
        end--;
    }

    printf("%d", res);
    return 0;
}