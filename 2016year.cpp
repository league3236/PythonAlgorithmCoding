#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

int main(){
    int a=2;
    int b=15;

    string answer = "";
    vector<string> dayname = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    int monthdays[12] = {31,60,91,121,152,182,213,244,274,305,335,365};

    int daysize = dayname.size();
    if(a==1){
        answer=dayname[(b-1)%daysize];
    }else{
        int temp = monthdays[a-2];
        answer=dayname[(temp+(b-1))%daysize];
    }
 
    cout << answer << endl;
    return 0;
}
