#include <iostream>

// string.h 는 strlen 때문에 include 했는데, 사실 여러분이 직접 strlen
// 과 같은 함수를 만들어서 써도 됩니다.
#include <string.h>

class MyString {
  char* string_content;  // 문자열 데이터를 가리키는 포인터
  int string_length;     // 문자열 길이
  int memory_capacity;   // 현재 할당된 용량

 public:
  // 문자 하나로 생성
  MyString(char c);

  // 문자열로 부터 생성
  MyString(const char* str);

  // 복사 생성자
  MyString(const MyString& str);

  ~MyString();

  int length() const;
  int capacity() const;
  void reserve(int size);

  void print() const;
  void println() const;

  MyString& assign(const MyString& str);
  MyString& assign(const char* str);
  char at(int index);

  MyString& insert(int loc, const MyString& str);
  MyString& insert(int loc, const char* str);
  MyString& insert(int loc, char c);

  MyString& erase(int loc, int num);

  int find(int find_from, MyString& str) const;
  int find(int find_from, const char* str) const;
  int find(int find_from, char c) const;
  int compareContent(int find_from, MyString& str) const;
};

int MyString::find(int find_from, char c) const{
  MyString temp(c);
  return find(find_from,temp);
}
int MyString::find(int find_from, const char* str) const{
  MyString temp(str);
  return find(find_from, temp);
}
int MyString::compareContent(int find_from, MyString& str) const{
  for(int i= 0; i<= str.string_length; i++){
    if(str.string_content[i]!= string_content[i+find_from]){
      return -1;
    }
  }
  return find_from;
}
int MyString::find(int find_from, MyString& str) const{
  for(int i= find_from; i<string_length-str.string_length; i++){
    int result = compareContent(i, str);
    if(result != -1){
      return find_from;
    }
  }
}

MyString::MyString(char c) {
  string_content = new char[1];
  string_content[0] = c;
  memory_capacity = 1;
  string_length = 1;
}
MyString::MyString(const char* str) {
  string_length = strlen(str);
  memory_capacity = string_length;
  string_content = new char[string_length];

  for (int i = 0; i != string_length; i++) {
    string_content[i] = str[i];
  }
}

MyString& MyString::erase(int loc, int num){
  if(loc < 0 || loc > string_length){
    return *this;
  }
  int start = loc;
  for(int i=loc+num;i<string_length;i++){
    string_content[i-num] = string_content[i];
    start++;
  }
  for (int i=start; i<string_length;i++){
    string_content[i] = NULL;
  }
  string_length-=num;
  return *this;
}

// insert문은 다 Mystring을 새로 만들어서 Mystring을 인자로 받는 함수에서 다룬다.
MyString& MyString::insert(int loc, const char* str){
  MyString temp(str);
  return insert(loc, temp);
}
MyString& MyString::insert(int loc, char c){
  MyString temp(c);
  return insert(loc, temp);
}
MyString& MyString::insert(int loc, const MyString& str){
  if (loc < 0 || loc > string_length) return *this; // 이 값 자체를 dereference 해서 반환
  char* prev_string_content = string_content;
  if (string_length + str.string_length > memory_capacity){
    memory_capacity = string_length+str.string_length;
    string_content = new char[memory_capacity]; // make new array
  }
  for (int i=0; i<loc; i++){
    string_content[i] = prev_string_content[i];
  }
  for (int i=0; i<str.string_length; i++){
    string_content[i+loc] = str.string_content[i];
  }
  for (int i=loc; i<string_length; i++){
    string_content[i+str.string_length] = prev_string_content[i]; 
  }
  delete[] prev_string_content;
  string_length +=str.string_length;
  return *this;
}

MyString::MyString(const MyString& str) {
  string_length = str.string_length;
  memory_capacity = str.string_length;
  string_content = new char[string_length];

  for (int i = 0; i != string_length; i++) {
    string_content[i] = str.string_content[i];
  }
}

MyString::~MyString() { delete[] string_content; }
int MyString::length() const { return string_length; }

void MyString::print() const {
  for (int i = 0; i != string_length; i++) {
    std::cout << string_content[i];
  }
}
void MyString::println() const {
  for (int i = 0; i != string_length; i++) {
    std::cout << string_content[i];
  }

  std::cout << std::endl;
}

MyString& MyString::assign(const MyString& str) {
  if (str.string_length > memory_capacity) {
    // 그러면 다시 할당을 해줘야만 한다.
    delete[] string_content;

    string_content = new char[str.string_length];
    memory_capacity = str.string_length;
  }
  for (int i = 0; i != str.string_length; i++) {
    string_content[i] = str.string_content[i];
  }

  // 그리고 굳이 str.string_length + 1 ~ string_length 부분은 초기화
  // 시킬 필요는 없다. 왜냐하면 거기 까지는 읽어들이지 않기 때문이다.

  string_length = str.string_length;

  return *this;
}
MyString& MyString::assign(const char* str) {
  int str_length = strlen(str);
  if (str_length > memory_capacity) {
    // 그러면 다시 할당을 해줘야만 한다.
    delete[] string_content;

    string_content = new char[str_length];
    memory_capacity = str_length;
  }
  for (int i = 0; i != str_length; i++) {
    string_content[i] = str[i];
  }

  string_length = str_length;

  return *this;
}
int MyString::capacity() const { return memory_capacity; }
void MyString::reserve(int size) {
  if (size > memory_capacity) {
    char* prev_string_content = string_content;

    string_content = new char[size];
    memory_capacity = size;

    for (int i = 0; i != string_length; i++)
      string_content[i] = prev_string_content[i];

    delete[] prev_string_content;
  }

  // 만일 예약하려는 size 가 현재 capacity 보다 작다면
  // 아무것도 안해도 된다.
}

char MyString::at(int index){
  if (index>=string_length || index<0){
    return NULL;
  }
  return string_content[index];
}
int main() {
  MyString str1("this is a very very long string");
  std::cout << "Location of first <very> in the string : " << str1.find(0, "very")
       << std::endl;
  std::cout << "Location of second <very> in the string : " << str1.find(str1.find(0, "very") + 1, "very") << std::endl;
}