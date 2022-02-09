#include <iostream>
using namespace std;

void SWAP(char &i, char &j){
    char temp;
    temp = i;
    i = j;
    j = temp;
}

void Permutation(char* list, int i, int n){
    int j;
    if(i==n){
        for(j=0; j<=n;j++){
            cout<< list[j] << " ";
        }
        cout << endl;
    }
    else{
        for(j = i; j<=n;j++){
            SWAP(list[i], list[j]);
            Permutation(list, i+1, n);
            SWAP(*(list+i), *(list+j));
        }
    }
}

int main() {
    char list[3] = {'a', 'b', 'c'};
    int n = 3;
    Permutation(list, 0, n-1);
    return 0;
}
