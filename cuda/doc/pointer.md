### pointer란
포인터란 메모리의 주소값을 저장하는 변수이며, 포인턴 변수라고 불린다.
비유를 하자면 택배 아저씨의 역할을 한다고 보면 된다.    
#### 택배 아저씨의 비유
##### 1. 택배 아저씨가 하는 일
- 고객의 주소를 저장하고 있다가 해당 주소로 물건을 전달한다.
- 고객의 주소를 저장하고 있다가 해당 주소로 물건을 받아가는 일을 진행한다.
- 우리에게 '간접 접근'의 기능을 제공하는 셈이다.
##### 2. 택배 아저씨가 있어서 우리가 편리한 점
- 물품을 수령하기 위해서 구매처를 직접 방문하지 않아도 된다.
- 반품을 위해서 구매처를 직접 방문하지 않아도 된다.
##### 그렇다면 위 편리한 점을 컴퓨터에서의 작업으로 해석해보면
##### 🧑‍💻 이 택배 아저씨는 포인터 변수의 역할을 수행(포인터라고 부른다.)
1. 메모리의 주소를 저장하고 있다가 해당 주소로 데이터를 전달한다.
2. 메모리의 주소를 저장하고 있다가 해당 주소로 데이터를 참조한다.(접근)

### 포인터 연산자
1. 주소 연산자 (&)
- 주소 연산자는 변수의 주소값을 반환할 때 사용한다.
2. 참조 연산자 (*)
- 포인터에 가리키는 주소에 저장된 값을 반환한다.    
- 즉, 포인터 변수에 저장된 주소에 저장된 값을 가져온다는 뜻이다.

### 주소의 가감산
<pre>
<code>
int a =3;
int *pa = &a;
int **ppa = &pa;

cout << "a :\t" << a << endl;
cout << "&a :\t" << &a << endl;
cout << "pa :\t" << pa << endl;
cout << "&pa :\t" << &pa << endl;
cout << "*pa :\t" << *pa << endl;
cout << "ppa :\t" << ppa << endl;
cout << "*ppa :\t" << *ppa << endl;
cout << "**ppa :\t" << **ppa << endl;

</code>
</pre>
![Alt text](./images/pointerdouble.png "pointer result plus double pointer too")

### 함수 포인터
함수 포인터란 함수의 시작 주소를 저장하는 변수라고 한다.    
포인터를 선언하고 사용하는 방법은 기존 함수와 매우 유사하다.

#### 왜 사용하는가?
1. 일반적인 함수 호출보다 빠른 처리 속도를 기대할 수 있다.
2. 사용분야로 컴파일러, 인터프리터, 게임 프로그래밍 등의 시스템 프로그래밍 쪽
아래 간단한 사용법을 확인해보자.

<pre>
<code>
자료형 / 함수 포인터 이름 / 인수 자료형 목록 으로 선언해야 함
// 예시
void add (double num1, double num2) // 포인팅 대상 함수
void (*pointer) (double, double)  // 함수 포인터 선언을 이렇게 한다!!
pointer = add; // function pointer saves functions' initial address
pointer(3.1,5.1); // If we want to call with function pointer
</code>
</pre>
### void 포인터
- generic pointer라고 불린다.
- 모든 데이터 자료형을 가리킬 수 있는 특별한 타입의 포인터
- void 포인터는 void 키워드를 사용하여 일반 포인터처럼 선언한다. 👍
- void 포인터는 모든 데이터 자료형의 객체를 가리킬 수 있다.

<pre>
<code>
int nValue;
float fValue;

struct Something{
    int n;
    float f;
}

struct Something sValue;

void *ptr;
ptr = &nValue; // valid
ptr = &fValue; // valid
ptr = &sValue; // valid

</code>
</pre>

그런데 void 포인터는 어떤 데이터 자료형의 객체를 가리키는지에 대한 정보를 갖고 있지 않기 때문에 이전까지 썼던 방식으로 역참조가 안된다.💯      
역참조하기 전에 void 포인터를 먼저 특정 포인터 유형으로 type을 명시해줘야 한다 :desktop_computer: 

<pre>
<code>
int value = 5;
void * voidPtr = &value;
cout << *voidPtr << endl; // This won't work. This pointer doesn't know which type of value to read.
int *intPtr = static_cast<int*>(voidPtr); // We can cast the pointer to solve this problem.
cout << *intPtr << endl;
</code>
</pre>
Link1 : [pointer basic][https://natejin.tistory.com/28#--%--%ED%--%A-%EC%--%--%--%ED%-F%AC%EC%-D%B-%ED%--%B-]   
Link2 : [pointer advanced][http://soen.kr/]