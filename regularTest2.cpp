#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> one = {1,2,3,4,5};
vector<int> two = {2,1,2,3,4,2,5};
vector<int> thr = {3,3,1,1,2,2,4,4,5,5};

int main(){
    vector<int> answers;
    vector<int> answer;
    vector<int> they(3);
    for(int i=0; i<answers.size(); i++){
        if(answers[i] == one[i%one.size()]) they[0]++;
        if(answers[i] == one[i%two.size()]) they[1]++;
        if(answers[i] == one[i%thr.size()]) they[2]++;
    }
    int they_max = *max_element(they.begin(), they.end());
    for(int i =0 ; i<3; i++){
        if(they_max == they[i]) answer.push_back(i+1); 
    }
    
    return answer;
}

