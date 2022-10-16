#include <iostream>

using namespace std; 

int main(){
    // 구조체는 다른 데이터형을 허용되는 데이터의 집합
    struct student{ // 새로운 데이터 형을 만드는 것과 같음 
        string name;
        string position;
        int height;
        int weight;
    } C;
    student A; // student형 A라는 변수를 선언 
    A.name = "Kim";
    A.position = 'CB';
    A.height = 190;
    A.weight = 87;
    cout << A.height << endl;

    student B = {"Lee","LF",174,70};
    // C라는 건 이미 선언된거여서 그냥 쓸 수 있다.
    C.height = 200;
    C.weight = 100;
    C.name = "Temp";
    C.position ="UNKNOWN";
    return 0;
}