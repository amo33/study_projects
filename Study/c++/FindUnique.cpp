#include <iostream>

using namespace std;

int main(){
    
    cin.tie(0);
    int temp =0;
    int num = 0, flag =0;
    int account = 0;
    cin >> num;

    for(int i=0; i<num; i++){
        flag = 0;
        cin >> temp;
        for(int j=2; j*j <=temp; j++){
            if(temp % j == 0){
                flag = 1;
                break;
            }
                
        }
        if(flag == 1)
            account+=1;
        else
            continue;

    }
    cout << account << "\n";
}