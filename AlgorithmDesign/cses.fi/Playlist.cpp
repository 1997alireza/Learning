#include <iostream>
#include <queue>
#include <set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    scanf("%d", &n);
    deque<int> q;
    set<int> s;
    int max = 0;
    int temp;


    for (int ind = 0; ind < n; ind++) {
        scanf("%d", &temp);

        if(s.find(temp) != s.end()){
            s.erase(temp);
            while(!q.empty()){
                if(q[0] == temp){
                    s.erase(q[0]);
                    q.pop_front();
                    break;
                }
                else {
                    s.erase(q[0]);
                    q.pop_front();
                }
            }
        }
        q.push_back(temp);
        s.insert(temp);
        if(max < q.size()) max = (int)q.size();
    }

    printf("%d", max);
    return 0;
}