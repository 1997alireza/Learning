#include <iostream>
#include <algorithm>

#define Loop(i, n) for(int i = 0; i < n; i++)
#define LoopSh(i, n) for(short i = 0; i < n; i++)

using namespace std;

short getSh(char c){
    switch(c){
        case('C'):
            return 1;
        case('G'):
            return 2;
        case('T'):
            return 3;
    }
    return 0;
}

char getCh(short s){
    switch (s){
        case(1):
            return 'C';
        case(2):
            return 'G';
        case(3):
            return 'T';
    }
    return 'A';
}

int getlen(int last, int* leng){
//    last[[i+1][0]] -> -1 ==> LEN=0 , ow: len = len[last[i+1][0]]
    if(last == -1) return 0;
    return leng[last];
}

void print_seq(int** last, short* prev, int l){
    string r = "";
    int ind = l;
    r = r + getCh(prev[ind]);
    while(last[ind][prev[ind]] != -1){
        ind = last[ind][prev[ind]];
        r += getCh(prev[ind]);
//        r = getCh(prev[ind]) + r;
    }
    for(int i = r.size()-1; i >= 0; i--) cout << r[i];
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    int l = s.size();
    int **last;// [l+1][4]; // a, b, g, t
    last = new int*[l+1];
    last[0] = new int[4];
    short prev[l+1];
    int leng[l+1];
    last[0][0] = -1; last[0][1] = -1; last[0][2] = -1; last[0][3] = -1;
    prev[0] = 0;
    leng[0] = 1;
    short ii;
    Loop(i, l) {
        last[i+1] = new int [4];
        ii = getSh(s[i]);
        last[i+1][ii] = i;
        LoopSh(j, 3){
            last[i+1][(ii+j+1)%4] = last[i][(ii+j+1)%4];
        }


        int minL = getlen(last[i+1][3], leng);
        short minPrev = 3;

        LoopSh(j, 3){
            int ll = getlen(last[i+1][j], leng);
            if(ll < minL){
                minL = ll;
                minPrev = j;
            }
        }
        leng[i+1] = minL + 1;
        prev[i+1] = minPrev;
    }
    print_seq(last, prev, l);
    return 0;
}
