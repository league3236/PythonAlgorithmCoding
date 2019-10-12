#include <iostream>
#include <algorithm>

using namespace std;
const int MAX=1000000000;
int N;
int a[101];
int v[4];
int cnt=1;
int sum;
int maxResult=-MAX;
int minResult=MAX;

void input(){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> a[i];
    }
    for(int i=0;i<4;i++){
        cin >> v[i];
    }
    sum = a[0];
}

void dfs(int plus, int minus, int mul, int div, int cnt, int sum){
    if(cnt==N){
        maxResult=max(maxResult,sum);
        minResult=min(minResult,sum);
    }

    if(plus>0){
        dfs(plus-1, minus, mul, div, cnt+1, sum+a[cnt]);
    }
    if(minus>0){
        dfs(plus, minus-1, mul, div, cnt+1, sum-a[cnt]);
    }
    if(mul>0){
        dfs(plus, minus, mul-1, div, cnt+1, sum*a[cnt]);
    }
    if(div>0){
        dfs(plus, minus, mul, div-1, cnt+1,sum/a[cnt]);
    }
}

void output(){
    cout << maxResult << endl;
    cout << minResult << endl;
}

int main()
{
    input();
    dfs(v[0],v[1],v[2],v[3],1,a[0]);
    output();
    return 0;
}
