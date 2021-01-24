#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

int main(){
    vector<int> arr = {1,1,3,3,0,1,1};
    vector<int> answer;

    int start=arr[0];
    answer.push_back(start);
    for(vector<int>::iterator iter=arr.begin(); iter!=arr.end(); iter++){
        if(start!=*iter){
            start=*iter;
            answer.push_back(start);
        }
    }

    return answer;
}
