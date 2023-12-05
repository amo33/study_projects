/*
1. struct
 object와 class의 기반이 되는 개념이다.
 c structure는 여러 변수들을 다 갖고 있는 하나의 큰 변수다.
    사용 목적
    1. Data serialization
    2. 하나의 argument를 함수안에 넣어서 사실상 여러 개의 변수를 다 제어하고 싶을때
    3. Linked list, binary Tree등등을 만들 때 사용된다.

    가장 많이 쓰이는 예시는 point(좌표)다.
    아래와 같이 point라는 구조체를 사용해서 2개 이상의 변수를 제어할 수 있다.
    struct point{
        int x;
        int y;
    };

    struct point p;
    p.x = 10;
    p.y = 5;
    draw(p);
2. typedefs
 typedefs는 1번에 설명된 struct 구조체에 이름을 따로 명시해주는데 사용한다.
 가령 struct point 형으로 선언하면 귀찮기 때문에 그냥 'nameexample' 처럼 쓰일 수 있게 해준다.
    typedef struct {
        char * brand;
        int model;
    } vehicle;

    vechile mycar;
    mycar.brand = "Ford";
    mycar.model = 2007;
*/
