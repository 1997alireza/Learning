#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    scanf("%d", &n);
    int max, nw;
    scanf("%d", &max);
    long turn = 0;
    for(int i = 1; i < n; i++){
        scanf("%d", &nw);
        if(nw >= max){
            max = nw;
        }
        else{
            turn += (long)(max - nw);
        }
    }
    printf("%ld", turn);
    return 0;
}