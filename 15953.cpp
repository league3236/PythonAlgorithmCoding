#include <iostream>

using namespace std;

int test_case, a, b;
int sum_1, sum_2;
int coin;

int main()
{
    cin >> test_case;
    for(int j=0; j<test_case; j++){
        cin >> a >> b;
        coin=0, sum_1=21, sum_2=31;

        if(a>sum_1){
            coin+=0;
        }else if(a>(sum_1-=6)){
            coin+=10;
        }else if(a>(sum_1-=5)){
            coin+=30;
        }else if(a>(sum_1-=4)){
            coin+=50;
        }else if(a>(sum_1-=3)){
            coin+=200;
        }else if(a>(sum_1-=2)){
            coin+=300;
        }else if(a>(sum_1-=1)){
            coin+=500;
        }
        if(b>sum_2){
            coin+=0;
        }else if(b>(sum_2-=16)){
            coin+=32;
        }else if(b>(sum_2-=8)){
            coin+=64;
        }else if(b>(sum_2-=4)){
            coin+=128;
        }else if(b>(sum_2-=2)){
            coin+=256;
        }else if(b>(sum_2-=1)){
            coin+=512;
        }

    coin*=10*10*10*10;
    cout << coin << endl;
    }
    return 0;
}
