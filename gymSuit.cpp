#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int minus = lost.size();

    for(int i=0; i<lost.size(); i++){
        for(int j=0; j<reserve.size(); j++){
            if(lost[i]==reserve[j]) {lost.erase(lost.begin()+(i--)); reserve.erase(reserve.begin()+(j--)); minus--; break;}
        }
    }
    for(int i=0; i<lost.size(); i++){
        for(int j=0; j<reserve.size(); j++){
            if(lost[i]==reserve[j]-1 || lost[i]==reserve[j]+1) {lost.erase(lost.begin()+(i--)); reserve.erase(reserve.begin()+(j--)); minus--; break;}
        }
    }
    answer = n-minus;  
    return answer;
}

int main(){
    cout << solution(3,{3},{1}) << endl;
    return 0;
}
