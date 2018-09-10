#include <iostream>
#include <algorithm>
#include <set>

using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    scanf("%d%d", &n, &m);
    multiset<int> s;
    int temp;
    for(int i = 0; i < n; i++) {
        scanf("%d", &temp);
        s.insert(temp);
    }
    for(int i = 0; i < m; i++) {
        scanf("%d", &temp);
        if(!s.empty()) {
            auto p = s.upper_bound(temp);
            if(p != s.begin()) {
                p--;
                printf("%d\n", *p);
                s.erase(p);
            }
            else {
                printf("%d\n", -1);
            }
        }
        else{
            printf("%d\n", -1);
        }
    }

    return 0;
}