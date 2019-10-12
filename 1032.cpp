#include <iostream>
#include <string>

using namespace std;

int N;
string str[51];
string result;

void input(){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> str[i];
    }
}

void pattern(){
    for(int i=0; i<str[0].length(); i++){
        bool flag=true;
        string ap="";
        for(int j=0;j<N-1;j++){
            ap=str[j].at(i);
            if(str[j].at(i)!=str[j+1].at(i)){
                flag=false;
                break;
            }   
        }
        if(flag==false){
            result.append("?");
        }else{
            result.append(ap);
        }
    }
}

void output(){
    cout << result << endl;
}

int main()
{
    input();
    pattern();
    output();
    return 0;
}
