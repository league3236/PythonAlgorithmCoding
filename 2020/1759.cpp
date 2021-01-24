#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int L, C;
char arr[16];
string result;

void input(){
    cin >> L >> C;
    for(int i=0; i<C; i++){
        cin >> arr[i];
    }
    sort(arr,arr+C);
}

void dfs(int i, int mo, int ja, int cnt, string str){
    if(cnt==L){
        if(mo>=1 && ja>=2){
            cout << str << endl;
        }
        return;
    }
    if(i==C){
        return;
    }
    if(arr[i]=='a'||arr[i]=='e'||arr[i]=='i'||arr[i]=='o'||arr[i]=='u'||arr[i]=='a'){
            dfs(i+1,mo+1,ja,cnt+1,str+arr[i]);
    }
    else{
        dfs(i+1,mo,ja+1,cnt+1,str+arr[i]);
    }
    dfs(i+1,mo,ja,cnt,str);
}

void output(){
    cout << arr << endl;
}

int main()
{
    input();
    dfs(0,0,0,0,"");
    return 0;
}
