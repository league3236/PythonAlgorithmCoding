#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n=10;
    int answer=0;
    int test[1000000];

    for(int i=2; i<=n; i++){
        if(test[i]==0){
            answer++;
            int k=i;
            int j=1;
            while(k*j<=n){
                test[k*j]++;
                j++;
            }
        }
    }
    cout << answer;
    return 0;
}
