#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    vector<string> seoul={"Jane", "Kim"};
    string answer = "";
    int i=0;
    for(string iter:seoul){
        if(iter=="Kim"){
            break;        
        }
        i++;
    }
    answer = "김서방은 "+to_string(i)+"에 있다";
    return 0;
}
