/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <queue>

using namespace std;

int N;
int graph[101][101];
int result[101][101];
int visited[101];

void input(){
    cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> graph[i][j];
        }
    }
} 

void output(){
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
} 

void bfs(int n){
    queue<int> q;
    q.push(n);
    
    while(!q.empty()){
        int first = q.front();
        for(int i=0;i<N;i++){
            if(graph[first][i]==1&&visited[i]==0){
                visited[i]=1;
                q.push(i);
            }
        }
        q.pop();
    }
}

void check(int n){
    for(int i=0; i<N; i++){
        if(visited[i]==1){
            result[n][i] = 1;
            visited[i]==0;
        }
    }
    
}

int main()
{
    input();
    for(int i=0;i<N;i++){
        bfs(i);
        check(i);
    }
    output();
    return 0;
}
