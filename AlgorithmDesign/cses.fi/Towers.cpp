#include <iostream>
#include <algorithm>
#include <vector>
#include <list>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    scanf("%d", &n);
    vector<int> towers;
    int temp;
    scanf("%d", &temp);
    towers.push_back(temp);
    for(int i = 1; i < n; i++){
        scanf("%d", &temp);
        auto p = upper_bound(towers.begin(), towers.end(), temp);
        if(p >= towers.end()){
            towers.push_back(temp);
        }
        else{
            *p = temp;
        }
    }

    printf("%d", towers.size());
    return 0;
}