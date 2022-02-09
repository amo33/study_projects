#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> arr;
vector<int> temp_list;
static int cnt(0);

void SWAP(int &a, int &b){
    int temp_swap(0);
    temp_swap =a;
    a = b;
    b = temp_swap;
    cnt++;
}

void merge_sort(int start, int middle, int end){

    sort(arr.begin()+start, arr.begin()+middle);
    for(int j =0; j< middle-start-1;j++){
        for(int i = start; i<middle-1-j;i++){
            if(arr[i]>arr[i+1]){
                SWAP(arr[i], arr[i+1]);

            }
        }
    }
    for(int j =0; j< end-middle-2;j++){
        for(int i = middle+1; i<end-1-j;i++){
            if(arr[i]>arr[i+1]){
                SWAP(arr[i], arr[i+1]);
            }
        }
    }

    while(!arr.empty()){
        if(arr[start] < arr[middle+1]){
            temp_list.push_back(arr[start]);

        }
        else{
            temp_list.push_back(arr[middle+1]);

        }
    }
}

void merge(int start, int end){
    if(start < end){
        int middle((start+end)/2);
        merge(start, middle);
        merge(middle+1, end);
        merge_sort(start, middle, end);
    }


}

int main() {

    int N(0);
    int temp(0);

    cin >> N;

    for(int i=0;i<N;i++){
        cin >> temp;
        arr.push_back(temp);
    }
    /*
    for(auto a : arr){
        cout << a << " ";
    }
    cout << endl;
    */
    merge(0, arr.size());
    cout << cnt << endl;



    return 0;
}
