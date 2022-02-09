#include <iostream>

using namespace std;

long long times(long long a,long long b){
    long long tmp;
    if(b > 1){
        tmp = times(a, b/2);
    }
    if(b==1){
        return a;
    }
    if(b % 2 ==1)
        return (tmp * a * tmp);

    else if(b % 2 ==0){
        return (tmp*tmp);
    }

}

int main() {
    long long num(0), time(0), division(0);
    cin >> num;
    cin >> time;
    cin >> division;
    cout << times(num,time) % division << endl;

    return 0;
}
