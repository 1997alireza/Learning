#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    int m = 0;
    int k = 0;
    for(int i = 1; i < s.size(); i++){
        if(s[i] == s[i-1]){
            k++;
        }
        else{
            if(k > m) m = k;
            k = 0;
        }
    }
    if(k > m) m = k;
    printf("%d", m+1);
    return 0;
}