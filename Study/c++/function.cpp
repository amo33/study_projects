#include <iostream>

using namespace std;
struct Time{
    int hour;
    int min;
}; 
Time sum(Time* t1, Time* t2){
    Time total;
    total.min = (t1->min + t2->min) % PerHr; 
    total.hour = (t1->hour + t2->hour + (t1->min + t2->min) / PerHr 
    );
    return total; 
}
int calculateValue(int a){
    return a*3; // returns int value
}
const int PerHr = 60; 
void showTime(Time t){
    cout << "Hour is " << t.hour << " and minute is " << t.min << endl;
}
int main(){
    int val;
    cout << "Get int value\n";
    cin >> val;
    cout << calculateValue(val) << endl;
    Time d1 = {5, 45};
    Time d2 = {4, 55};
    Time total = sum(&d1 , &d2);
    
    return 0; 
}