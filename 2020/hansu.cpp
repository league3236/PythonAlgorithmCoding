#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int answer=0;
int hansu(int n){
    for(int i=1;i<=n;i++){
        if(i<100){
            answer++;
        }else if(i<1000){
            if(((i/10)%10-i/100)==(i%10)-(i/10)%10){
                answer++;
            }
        }
    }
    return answer;
}

int main(){
    int n=999;
    cout << hansu(n);
    return 0;
}
