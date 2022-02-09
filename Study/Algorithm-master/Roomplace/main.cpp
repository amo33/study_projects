#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct conference{
    int start;
    int finish;
    conference(int a, int b) : start(a), finish(b) {}
};
// 질문하기 //
bool operator<(conference a, conference b){
    if(a.finish == b.finish){
        return a.start < b.start;
    }
    return a.finish < b.finish;
}

int main() {
    int N;
    cin >> N;
    vector<conference> vec;

    for(int i=0; i<N;i++){
        int start_time(0); int Finish_time(2^31 -1);
        cin >> start_time >> Finish_time;
        vec.push_back(conference(start_time, Finish_time));
    }
    sort(vec.begin(), vec.end());

    int answer(1);
    int before_conference(0);
    for(int i = 1; i<N;i++){
        if(vec[i].start >= vec[before_conference].finish){
            before_conference = i;
            answer++;
        }
    }
    return 0;
}
