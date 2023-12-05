/*
Dynamic allocation : 동적 할당
-> Allows Building complex data structures (linked list)
-> 동적 할당을 통해 크기를 미리 제한해두고 개발하지 않아도 된다.
-> runtime에 결정되기 때문이다.

 typedef struct {
    char *name;
    int age;
 }person;
 
 //새로운 person을 만들려면 아래와 같이 사용
 person * myperson = (person *)malloc(sizeof(person));
 myperson->name = "John";
 myperson->age = 27;
 free(myperson);

 
*/

