#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>

using namespace std;

int main(){
    vector<string> record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
    vector<string> answer;

    map<string, string> idrec;
    
    for(vector<string>::iterator iter=record.begin(); iter!=record.end(); iter++){
        stringstream ss(*iter);
        string cmd, uid, name;
        ss >> cmd;
        if(cmd.compare("Enter")==0){
            ss >> uid >> name;
            idrec[uid] = name;
        }else if(cmd.compare("Change")==0){
            ss >> uid >> name;
            idrec[uid] = name;
        }
    }

    for(vector<string>::iterator iter=record.begin(); iter!=record.end(); iter++){
        stringstream ss(*iter);
        string cmd, uid, name;
        ss >> cmd;
        if(cmd.compare("Enter")==0){
            ss >> uid >> name;
            answer.push_back(idrec[uid]+"님이 들어왔습니다.");
        }else if(cmd.compare("Leave")==0){
            ss >> uid;
            answer.push_back(idrec[uid]+"님이 나갔습니다.");
        }
    }


    return 0;
}
