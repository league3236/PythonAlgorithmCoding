#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    string s="1234";
    bool answer = true;
    int length = s.length();
    if(length==4||length==6){
        answer=true;
    }
    for(int i=0;i<s.length();i++){
        if(s[i]>'9'||s[i]<'0'){
            answer=false;
            break;
        }
    }
    cout << answer << endl;

    return 0;
}
