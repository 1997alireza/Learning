#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    scanf("%d", &t);
    int x,y, temp;
    long max;
    for(;t > 0; t--){
        scanf("%d%d", &y, &x);
        max = (x > y)? x:y;
        if(max%2 == 0) {
            temp = x;
            x = y;
            y = temp;
        }
        if(x <= y){
            printf("%ld\n", (max-1)*(max-1) + x);
        }
        else{
            printf("%ld\n", max*max - y + 1);
        }
    }
    return 0;
}