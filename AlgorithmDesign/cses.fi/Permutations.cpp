#include <iostream>
#define NO_SOL "NO SOLUTION"
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    scanf("%d", &n);
    if(n == 2 or n== 3) printf(NO_SOL);
    else {
        for (int i = 0; i < n / 2; i++) printf("%d ", i * 2 + 2);
        for (int i = 0; i < n / 2; i++) printf("%d ", i * 2 + 1);
        if (n % 2 != 0) printf("%d", n);
    }
    return 0;
}