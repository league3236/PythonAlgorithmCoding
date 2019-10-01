#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

#define MIN(a,b) a>b?b:a

int N, K;
long double M;
long double answer;
long double arr[501];
long double sum;
int main()
{
    answer = 9999999.9;
    cin >> N >> K;

    for(int i=0; i<N ;i++){
        cin >> arr[i];
    }
    for(int i=0;i<=N-K;i++){
        for(int k=K; k<=N-i; k++){
            sum = 0.0;
            M = 0.0;
            for(int j=i;j<i+k;j++){
                sum+=arr[j];
            }
            M=sum/(long double)k;
            long double dsum=0.0;
            for(int j=i;j<i+k;j++){
                dsum+=pow(arr[j]-M,2);
            }
            answer = MIN(answer, sqrt(dsum/(long double)k));
        }
    }

    printf("%.11Lf\n",answer);

    // M=sum/(long double)N;
    // answer=0.0;
    // for(int i=0; i<N ;i++){
    //     answer+=pow(arr[i]-M,2);
    // }
    // answer/=(long double)N;

    // cout << sqrt(answer) << endl;
    
    return 0;
}
