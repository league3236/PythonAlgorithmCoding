#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

// int solution(int n, vector<int> lost, vector<int> reserve) {
      
//     return answer;
// }

int main(){
    vector<int> array = {1, 5, 2, 6, 3, 7, 4};
    vector<vector<int>> commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

    vector<int> answer;
    
    for(int i=0; i<commands.size(); i++){
        
        vector<int> li;
        int one = commands[i][0], two=commands[i][1], three=commands[i][2];
        
        for(int j=one-1; j<two; j++){
            li.push_back(array[j]);
        }
        sort(li.begin(), li.end());

        answer.push_back(li[three-1]);
        // for(vector<int>::iterator iter=li.begin(); iter!=li.end(); iter++){
        //     cout << *iter << endl;
        // }

    }
    return answer;
}
