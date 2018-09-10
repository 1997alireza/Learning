#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n_apc, n_aprt, dif, i;
    scanf("%d%d%d", &n_apc, &n_aprt, &dif);
    int apc[n_apc], aprt[n_aprt];
    for(i = 0; i < n_apc; i++) scanf("%d", apc+i);
    for(i = 0; i < n_aprt; i++) scanf("%d", aprt+i);
    sort(apc, apc+n_apc);
    sort(aprt, aprt+n_aprt);
    int res = 0;
    int apc_it = 0;
    for(i = 0; i < n_aprt; i++){ // apc - dif <= aprt <= apc + dif
        while(apc_it < n_apc and apc[apc_it] + dif < aprt[i]) apc_it++;
        if(apc_it == n_apc) break;
        if(apc[apc_it] - dif <= aprt[i]) {
            res++;
            apc_it++;
        }
    }
    printf("%d", res);
    return 0;
}