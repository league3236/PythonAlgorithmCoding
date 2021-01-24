#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int arr[9]={20, 7, 23, 19, 10, 15, 25, 8, 13};
    int result = 0;
    int a, b;
    int flag = false;
    for(int i=0;i<9;i++){
        cin >> arr[i];
        result+=arr[i];
    }
    
    
    for(int i =0; i<9; i++){
        for(int j =0; j<9; j++){
            if(i!=j&&result-(arr[i]+arr[j])==100){
                a = arr[i];
                b = arr[j];
                flag = true;
                break;
            }
        }
        if(flag==true){
            break;
        }
    }
    sort(arr, arr+9);
    
    for(int i=0;i<9;i++){
        if(a!=arr[i]&&b!=arr[i]){
            cout << arr[i] << endl;
        }
    }
    
    
   return 0;
}
