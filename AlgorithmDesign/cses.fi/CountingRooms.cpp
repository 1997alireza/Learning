#include <iostream>
#include <stdio.h>

using namespace std;

int n,m;
bool **floor;
void searchin(int x, int y){
    if(x<0 or y<0 or x>=n or y>=m) return;
    if(!floor[x][y]/* or seen[x][y]*/) return;
    floor[x][y] = false;
    searchin(x-1,y);
    searchin(x+1,y);
    searchin(x,y-1);
    searchin(x,y+1);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    scanf("%d%d", &n, &m);
    floor = new bool*[n];
    getchar();
    char temp;
    for(int i = 0; i < n; i++) {
        floor[i] = new bool[m];
        for (int j = 0; j < m; j++) {
            temp = getchar();
            floor[i][j] = (temp == '.');
        }
        getchar();
    }
    int num = 0;
    for(int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if(floor[i][j]/* && !seen[i][j]*/){
                num++;
                searchin(i,j);
            }
        }
    }

    cout << num;
    return 0;
}