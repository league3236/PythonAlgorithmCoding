#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

int main(){
    string s="abde";
    string answer = "";

    int leng = s.length();
    bool hol = leng%2;
    if(hol){
        answer = s.at(leng/2);
    }else{
        answer.push_back(s.at(leng/2-1));
        answer+=s.at(leng/2);
    }
    cout << answer << endl;

    return 0;
}
