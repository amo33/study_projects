#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
/*
int main() {
   int n(0), m(0), Inven(0);
   int need(0), remain(0);
   double sum(0);

   // cout << "What is n?:";
   cin >> n;
   // cout << "What is m?:";
   cin >> m;
   // cout << "How many in Inventory?:";
   cin >> Inven;
   // 2차원 배열을 선언하는 방법 with vector (2021.03.18)
   vector<vector<int>> arr(n,vector<int>(m));
   for(int i=0; i<n;i++){
       for(int j=0; j<m;j++){
           cin >> arr[i][j];
           sum += arr[i][j];
       }
   }
   sum /= n*m;

  // cout << sum << endl;
   sum = floor(sum + 0.5);
  // cout << sum << endl;

    for(int i=0; i<n;i++){
       for(int j=0;j<m;j++){
           int temp = sum;
           if(arr[i][j]<sum) {
               need += temp - arr[i][j];
           }
           else{
               remain += arr[i][j] - temp;
           }
       }
   }
   if(need > Inven + remain){
       // remain 값을 얼만큼 더해야하는지.. 그에 따라 그건 *2 하면 된다.
       int key = ceil((need - Inven +remain)/n*m);
       cout << key<<endl;
       cout << remain *2 + need + 2*(need - Inven +remain) << " ";
       cout << sum - key << endl;
   }
   else{
       cout << need  + remain * 2 << " ";
       cout << sum << endl;

   }

   /*
    for(int i=0; i<n;i++){
        for(int j=0; j<m;j++){
            cout << arr[i][j] << " ";
            sum += arr[i][j];
        }
        cout<< endl;
    }
    */
    /*return 0;
}
*/
int main(void){
    int n(0), m(0), inventory(0);

    int ans_time = 987654321;
    int ans_layer = -1;

    cin >>n;
    cin >>m;
    cin >> inventory;

    vector<vector<int>> arr(n,vector<int>(m));
    for(int i=0; i<n;i++){
        for(int j=0; j<m;j++){
            cin >> arr[i][j];

        }
    }
    for(int now_layer = 256; now_layer>=0; now_layer--){
        int now_time = 0;
        int now_inventory(inventory);

        for(int i =0; i<n;i++){
            for(int j = 0; j<m;j++){
                if(arr[i][j] > now_layer){
                    now_inventory+= (arr[i][j] - now_layer);
                    now_time +=(arr[i][j] - now_layer) *2;
                }
                else if(arr[i][j] < now_layer){
                    now_inventory -= (now_layer - arr[i][j]);
                    now_time +=(now_layer - arr[i][j]);
                }
            }
        }

        if(now_inventory <0) continue;
        if(now_time < ans_time) ans_time = now_time, ans_layer = now_layer;
    }
    cout << ans_time << " " << ans_layer << endl;

}