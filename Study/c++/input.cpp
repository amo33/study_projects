#include <iostream>
#include <cstring>

using namespace std;
int main(){
    const int Size = 15;
    char name1[Size];
    char name2[Size] = "C++programming";

    cout << "Hello my name is " << name2;
    cout << "what is your name?\n";

    cin.getline(name1, Size);
    cout << "Oh, " << name1 << "  your name starts with ";
    cout << name1[0] << " and your name length is" << strlen(name1) << "\n";
    cout << "allocated byte is " << sizeof(name1) << "\n";
    name1[3] = '\0';
    cout << "Your new name is" << name1 << endl;

    // string 
    string str1;
    string str2 = "panda"; 
    str1 = str2; //string은 다른 변수에 다른 변수 것을 저장할 수 있다. 그리고 배열처럼 사이즈를 지정하지 않아도 된다.
    cout <<str1[0] << endl; 
    return 0; 
}