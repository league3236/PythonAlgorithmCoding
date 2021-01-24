#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n=10;
    int answer=0;
    
    for(int i=2; i<=n; i++){
        int half;
        if(i%2==0) half=i/2+1;
        else half=i/2+2;
        for(int j=2; j<=half; j++){
            if(j==half){
                answer++;
            }
            if(i%j==0){
                break; 
            }

        }
    }
    cout << answer;

    return 0;
}
