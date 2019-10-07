#include <iostream>

using namespace std;
int testcase;
int arr[101];
int tmp;

int main()
{
    cin >> testcase;
    for(int i=0; i<testcase; i++){
        int n;
        cin >> n;
        for(int j=i;j>i-n;j--){
            tmp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = tmp;
        }
        arr[i-n]=i+1;
    }
    for(int i=0;i<testcase;i++){
        cout << arr[i] << ' ';
    }
    cout << endl;
    return 0;
}
