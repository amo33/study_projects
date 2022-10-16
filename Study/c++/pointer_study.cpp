#include <iostream>

using namespace std;

struct Mystruct{
    char name[20];
    int age;
};

int main(){
    int val = 3; // 변수 선언 
    // runtime에 어떤 결정을 내릴 수 있는게 객체지향의 장점
    // - array를 만드는 경우 
    // 절차적 프로그래밍의 경우 배열의 크기를 꼭 특정지어 알아야한다.
    // 객체 프로그래밍의 경우 배열의 크기를 runtime에 결정될 수 있다.
    cout << &val << endl;

    // 간접값 연산자 * 사용해서 포인터 연산,,
    // 이 연산자는 사용할 주소에다가 이름을 붙인다.  
    int *a; // c 
    int* b; // c++

    int c = 6; 
    b = &c; // 사용할 주소에다가 이름을 붙인다.

    cout << "c value " << c << endl;
    cout << "b value " << *b << endl;

    cout << "c address " << &c << endl; 
    cout << "b address " << b << endl; 
    // new 연산자는 자동으로 메모리 블록을 할당해주는 것을 의미 

    int* pointer = new int;  // 4byte 만큼을 지정해줘서 pointer로 리턴, 사용자가 메모리 조절을 알아서 잘할 수 있다.
    double* pointerArray = new double[3];
    pointerArray[0] = 0.2;
    pointerArray[1] = 0.5;
    pointerArray[2] = 0.8;
    cout << "First element is "<< pointerArray[0] << endl;
    pointerArray = pointerArray +1 ; // 주소값을 한 개씩 민다. 

    cout << pointerArray[0] << "and the second one is " << pointerArray[1] << endl; 
    delete[] pointerArray;
    delete pointer; // 할당된 pointer 메모리를 풀어준다.  

    Mystruct* temp = new Mystruct;

    cout << "What is your name?\n";
    cin >> (*temp).name; // temp->name

    cout <<  "How old are you?\n";
    cin >> (*temp).age; // temp->age 

    cout << "Hello " << (*temp).name << ", your age is " << temp->age << endl;    
    return 0;
}