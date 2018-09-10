#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    scanf("%d", &n);
    if(n%4 == 0){
        printf("YES\n%d\n", n/2);
        for(int i = 0; i < n/4; i++){
            printf("%d %d ", 4*i+1, 4*i+4);
        }
        printf("\n%d\n", n/2);
        for(int i = 0; i < n/4; i++){
            printf("%d %d ", 4*i+2, 4*i+3);
        }
    }
    else if(n%4 == 3){
        printf("YES\n%d\n", n/2+1);
        printf("1 2 ");
        for(int i = 1; i < n/4+1; i++){
            printf("%d %d ", 4*i, 4*i+3);
        }
        printf("\n%d\n", n/2);
        printf("3 ");
        for(int i = 1; i < n/4+1; i++){
            printf("%d %d ", 4*i+1, 4*i+2);
        }
    }
    else{
        printf("NO");
    }
    return 0;
}