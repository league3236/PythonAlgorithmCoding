#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int a=3, b=5;
    long long answer = 0;
    
    if(a>b){
        int tmp;
        tmp=a;
        a=b;
        b=tmp;
    }
    for(int i=a; i<=b; i++){
        answer+=i;
    }
    cout << answer << endl;

    return 0;
}
