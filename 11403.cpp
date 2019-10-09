#include <iostream>

using namespace std;
int graph[101][101];
int result[101][101];
int visited[101];
int N;

void input(){
    cin >> N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> graph[i][j];
        }
    }
}

void output(){
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cout << result[i][j] << ' ';
        }
        cout << endl;
    }
}

void dfs(int n){
    for(int i=0; i<N; i++){
        if(graph[n][i] && !visited[i]){
            visited[i]=1;
            dfs(i);
        }
    }
}

void check(int n){
    for(int i=0; i<N; i++){
        if(visited[i]){
            result[n][i]=1;
            visited[i]=0;
        }
    }
}

int main()
{
    input();
    for(int i=0; i<N; i++){
        dfs(i);
        check(i);
    }

    output();
    return 0;
}
