#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int N(0);
    int temp(0);
    int sum(0);
    vector<int> A;
    vector<int> B;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> temp;
        A.push_back(temp);
    }
    for(int i=0;i<N;i++){
        cin >> temp;
        B.push_back(temp);
    }
    //재배치시키지 않아야한다고 했는데,, sort 하는 것은 재배치가 아닌가요?
    sort(A.begin(), A.end(), greater<int>());
    sort(B.begin(), B.end());
    for(int i = 0; i< N;i++){
        sum += A[i] * B[i];
    }
    cout << sum << endl;
    return 0;
}
