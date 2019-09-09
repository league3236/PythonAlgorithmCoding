// 바이너리 배열(원소를 0, 1만 갖는 배열)이 주어졌을 때, 배열을 정렬하시오
// 단, 시간 복잡도는 O(n), 공간 복잡도는 O(1).
// 결과는 0이 먼저 출력되고 1이 출력되어야 합니다.
// Input: [1, 0, 1, 0, 1, 0, 0, 1]
// Output: [0, 0, 0, 0, 1, 1, 1, 1]

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int answer[]={1, 0, 1, 0, 1, 0, 0, 1};
    int kbin[sizeof(answer)/sizeof(answer[0])]={0,};
    int a=0;
    for(int i=0; i<sizeof(answer)/sizeof(answer[0]); i++){
        if(answer[i]==1){
            kbin[a++]=1;
        }
    }
    for(int i=0; i<sizeof(kbin)/sizeof(kbin[0]) ;i++){
        cout << kbin[i];
    }
    cout << endl;

    return 0;
}
