#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>
using namespace std;
class Course {
    int id;
    char instructor[100];
    int Roomnum;
};

class Student {
private:
    char Name[100];
    int Num = 0;
    Course course[10];
public:

    Student(const char* name, int n) {

    }
    char* getname() {
        return Name;
    }
    int getNumber() {
        return Num;
    }
    Course* getcourse() {
        return course;
    }
    void setname(const char* name) {
        strcpy(Name,name);
    }
    void setcourse(char const* coname) {
        // strcpy(course,coname);
    }
    int setnumber(int n) {
        Num = n;
    }
};

int main() {
    int a(0);
    cout << "How many students?:";
    cin >> a;
    string b;
    char* p = new char;
    cout << "Name:";
    cin >> *p;
    cout << b;
    Student st1(p, 3);
    puts(st1.getname());
    delete p;
}