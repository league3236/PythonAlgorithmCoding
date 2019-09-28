#include <iostream>
#include <string>
#include <list>

using namespace std;

int main()
{
    for(int i=0; i<3 ;i++){
        string a;
        cin >> a;
        int sum=1, answer=1;
        list<int> arr;
        bool flag=false;
    
        for(int i=1; i<a.length(); i++){
            if(a[i-1]==a[i]){
                flag=true;
                sum++;
            }
            if(a[i-1]!=a[i]){
                sum=1;
            }
            if(answer<sum){
                    answer=sum;
            }
        }
        cout << answer << endl;
    }
    
    return 0;
}
