#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    string s="pPoooy";
    int key=0;
    bool answer = true;

    for(int i=0; i<s.size(); i++){
        if(s[i]=='p'||s[i]=='P'||s[i]=='y'||s[i]=='Y'){
            if(s[i]=='p'||s[i]=='P'){
                key++;  
            }else{
                key--;
            }
        }
    }
    if(key!=0){
        answer=false;
    }

    cout << answer << endl;
    return 0;
}
