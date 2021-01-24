#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    vector<int> arr = {3,2,6};
    int divisor = 10;


    vector<int> answer;
    for(vector<int>::iterator iter=arr.begin();iter!=arr.end();iter++){
        if(*iter%divisor==0){
            answer.push_back(*iter);
        }
    }
    sort(answer.begin(),answer.end());
    if(answer.empty()){
        answer.push_back(-1);
    }

    return 0;
}
