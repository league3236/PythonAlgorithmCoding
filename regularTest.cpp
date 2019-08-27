#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    vector<int> answer;
    vector<int> answers = {1,2,3,4,5};
    int size = answers.size();
    int supo_one[] = {1, 2, 3, 4, 5};
    int supo_two[] = {2, 1, 2, 3, 2, 4, 2, 5};
    int supo_three[] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    int one_sum, two_sum, three_sum, maxt;
    

    cout << sizeof(supo_two)/sizeof(*supo_two) << endl;
    for(int i=0; i < size; i++){
        if(supo_one[i%(sizeof(supo_one)/sizeof(*supo_one))]==answers[i]) one_sum++;
        if(supo_two[i%(sizeof(supo_two)/sizeof(*supo_two))]==answers[i]) two_sum++;
        if(supo_three[i%(sizeof(supo_three)/sizeof(*supo_three))]==answers[i]) three_sum++;            
    }
    maxt = max({one_sum, two_sum, three_sum});
    if(one_sum == maxt || maxt == 0) answer.push_back(1);
    if(two_sum == maxt || maxt == 0) answer.push_back(2);
    if(three_sum == maxt || maxt == 0) answer.push_back(3);

    return 0;
}

