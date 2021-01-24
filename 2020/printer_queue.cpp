#include <iostream>
#include <queue>

using namespace std;

int testcase;
int main()
{
    cin >> testcase;
    for(int k=0; k<testcase; k++){
        int answer = 0, docu_num=0, important=0;
        queue<pair<int, int>> q;
        priority_queue<int> pq;

        cin >> docu_num >> important;

        for(int i=0; i<docu_num; i++){
            int docu_value=0;
            cin >> docu_value;
            q.push({i,docu_value});
            pq.push(docu_value);
        }

        while(!q.empty()){
            int idx = q.front().first;
            int val = q.front().second;
            
            if(val==pq.top()){
                pq.pop();
                q.pop();
                answer++;
                if(idx==important){
                    cout << answer << endl;
                    break;
                }
            }
            else{
                q.push({idx,val});
                q.pop();
            }
        }
        
    }
   return 0;
}
