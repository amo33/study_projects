#include <iostream>

using namespace std;

class Stock{
private:
    string name;
    int shares; 
    float share_val;
    double total_val;
    void set_total(){total_val = shares * share_val;}
public:
    void acquire(string&, int, float);
    void buy(int, float);
    void sell(int, float);
    Stock update(float);
    void show();
    Stock topVal(Stock&);
    Stock(string , int , float);
    Stock();
    ~Stock();
};
void Stock::acquire(string& co, int n, float pr){
    name = co;
    shares = n;
    share_val = pr;
    set_total();
}
void Stock::buy(int n, float pr){
    shares += n;
    share_val = pr;
    set_total();
}
void Stock::sell(int n, float pr){
    shares -= n ;
    share_val = pr;
    set_total();
}
Stock Stock::update(float pr){
    share_val = pr;
    set_total();
}
void Stock::show(){
    cout << "회사 평 : " << name << endl; 
    cout << "주식 수 : " << shares << endl;
    cout << "주가 : " << share_val << endl;
    cout << "Total value : " << total_val << endl;
}
Stock::Stock(string co, int n, float pr){
    // might make a constructor to do specific something if instance is created
    name = co;
    shares = n; 
    share_val = pr; 
    set_total();
}

Stock::Stock(){
    // might make a constructor to do specific something if instance is created
    name = "";
    shares = 0; 
    share_val = 0; 
    set_total();
}
Stock Stock::topVal(Stock &s){
    if(s.share_val > share_val)
        return s;
    else return *this; // this는 주소를 가리키기 때문에 값들을 넘기려면 *붙인다.
}
Stock::~Stock(){

}
int main(){
    Stock temp("Tiger", 100, 1000); // initiate // after using this instance collector destories
    temp.show();
    temp.buy(10, 1200);
    temp.show();
    temp.sell(5, 800);
    Stock temp2("C",20,1200);
    cout << "The bigger one is ";
    temp.topVal(temp2).show();
    return 0;
}