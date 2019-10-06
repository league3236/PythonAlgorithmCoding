#include <iostream>
#include <list>

using namespace std;
int testcase;
int arr[101]={0,1,1,3,2};
int answer[101]={0,};

int main()
{
    // cin >> testcase;
    testcase = 5;
    for(int i=0; i<testcase; i++){
        while(1){
            if(answer[i-arr[i]]==0){
                break;
            }
            for(int j=i-arr[i];j<101;j++){
                arr[j+1]=arr[j];
            }
        }
        answer[i-arr[i]] = i+1;
        for(int j=0; j<5; j++){
            cout << answer[j] << ' ';
        }
        cout << endl;
    }
    return 0;
}
