#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int n = 1;
vector<string> strings = {"sun", "bed", "car"};

bool mysort(string a, string b){
    if(a.at(n)!=b.at(n)){
        return a.at(n)<b.at(n);
    }else{
        return a<b;
    }
}

int main(){
    vector<string> answer;
    answer=strings;

    sort(answer.begin(),answer.end(),mysort);
    
    return 0;
}
