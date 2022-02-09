#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> list;
vector<int> temp_list;

void merge(int start, int middle, int end){
    sort(list.begin()+start, list.begin()+middle);
    sort(list.begin()+middle+1, list.begin()+end);
    while(!list.empty()){
        if(list[start] < list[middle+1]){
            temp_list.push_back(list[start]);

        }
        else{
            temp_list.push_back(list[middle+1]);

        }
    }
}

void merge_sort(int start, int end){
    if(start< end){
        int mid = (start+end)/2;
        merge_sort(start, mid);
        merge_sort(mid+1, end);
        merge(start, mid, end);
    };

}

int main() {

    int N(100);
    int temp(0);
    cout << "How long? :";
    cin >> N;
    cout << "While " << "\""<< N << "\""<< " keep typing elements:";
    for(int i =0; i<N;i++){
        cin >> temp;
        list.push_back(temp);
    }
    merge_sort(0, N);
    int n(0);
    for(auto a : temp_list){
        list[n] = a;
        cout << list[n]<<endl;
        n++;
    }
    return 0;
}
// Time complexity = O(n logn)
// space complexity = O(n)