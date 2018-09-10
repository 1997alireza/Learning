#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    scanf("%d", &n);
    int x;
    bool t[n+1] = {0};
    for(int i = 1; i < n; i++){
        scanf("%d", &x);
        t[x] = true;
    }
    for(int i = 1; i <= n; i++){
        if(!t[i]) {
            printf("%d", i);
            break;
        }
    }
    return 0;
}