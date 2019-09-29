
#include <iostream>
#include <vector>

using namespace std;

vector<vector<char>> map;
vector<vector<int>> visited;

int Row, Col;
int Row_Dir[4]={1,-1,0,0}, Col_Dir[4]={0,0,1,-1};

int count_sheep;
int count_wolf;
int total_count_sheep;
int total_count_wolf;

void dfs(int yRow, int xCol){
    if(map[yRow][xCol]=='o'){count_sheep++;}
    else if(map[yRow][xCol]=='v'){count_wolf++;}

    
    for(int i=0; i<4; i++){
        int new_Row = yRow+Row_Dir[i];
        int new_Col = xCol+Col_Dir[i];
        if(new_Row<0||new_Row>=Row||new_Col<0||new_Col>=Col){
            continue;
        }
        if(map[new_Row][new_Col]=='#' || visited[new_Row][new_Col]){
            continue;
        }
        visited[new_Row][new_Col]++;
        dfs(new_Row, new_Col);
    }

}


int main()
{
    cin >> Row >> Col;

    map = vector<vector<char>> (Row,vector<char>(Col,0));
    visited = vector<vector<int>> (Row,vector<int>(Col,0));
    total_count_sheep=0;
    total_count_wolf=0;

    for(int i=0; i<Row; i++){
        for(int j=0; j<Col; j++){
            cin >> map[i][j];
        }
    }

    for(int i=0; i<Row; i++){
        for(int j=0; j<Col; j++){
            if(map[i][j]!='#' && !visited[i][j]){
                visited[i][j]++;
                count_sheep=0;
                count_wolf=0;
                dfs(i, j);

                if(count_sheep > count_wolf) {total_count_sheep+=count_sheep;}
                else{total_count_wolf+=count_wolf;}
            }
        }
    }
    cout << total_count_sheep << ' ' << total_count_wolf;

    return 0;
}
