
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    string s="Zbcdefg";
    string answer = s;
    sort(answer.begin(),answer.end(),greater<char>());

    cout << answer << endl;
    return 0;
}
