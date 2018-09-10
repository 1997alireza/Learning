#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    vector<int> k;
    int n, temp;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp);
        auto p = lower_bound(k.begin(), k.end(), temp);
        if(p == k.end()) k.push_back(temp);
        else *p = temp;
    }

    cout << k.size();

    return 0;
}