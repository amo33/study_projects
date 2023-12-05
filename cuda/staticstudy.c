// static : 변수들은 스코프 범위를 결정할 때 사용된다. 
// 변수들은 static으로 선언될 수 있다. -> 접근 범위를 넓힐 수 있다.

/*

#include<stdio.h>
int runner() {
    int count = 0;
    count++;
    return count;
}

int main()
{
    printf("%d ", runner());
    printf("%d ", runner());
    return 0;
}
이 코드에서 count는 1씩 늘어나지 않고 계속 1만 출력한다. -> 함수 호출할 때마다 지역변수처럼 사용되어서 1로만 나오는 것

해당 문제를 해결하려면 static을 사용할 수 있다.

#include<stdio.h>
int runner()
{
    static int count = 0;
    count++;
    return count;
}

int main()
{
    printf("%d ", runner());
    printf("%d ", runner());
    return 0;
}

*/

// static function
// C에서 함수들은 default로 global이다. 만약 static 키워드로 선언하면 해당 함수는 특정 파일에서만 사용되는 것 -> 다른 소스 파일에서 해당 함수를 사용 안하기 위해서는 static을 사용해야 한다.
// static vs global : 얼만큼 해당 함수나 변수를 갖고 접근하고 있을것인가에 대한 지정
/*

static void fun(void) {
   printf("I am a static function.");
}

*/
