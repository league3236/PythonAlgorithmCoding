#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            answer+=' ';
        }else{
            if(s[i]>='a'&&s[i]<='z'&&(s[i]+n)>'z'||s[i]>='A'&&s[i]<='Z'&&(s[i]+n)>'Z'){
                answer += s[i]+n-26;
            }else{
                answer += s[i]+n;
            }
        }
    }
    return answer;
}
