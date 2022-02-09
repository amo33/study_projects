#include <stdio.h>
static int cnt = 0;
void hanoi(int n, char start, char temp, char end){
    cnt ++;
    if(n==1){
        printf("%d th plate moves from %c to %c \n ", n, start, end);
        return;
    }

    hanoi(n-1, start, end, temp);
    printf("%d th plate moves from %c to %c\n ", n, start, end);
    hanoi(n-1, temp, start, end);
}


int main() {
    int N(0);
    printf("How many plates?:");
    scanf("%d", &N);
    hanoi(N, 'A', 'B', 'C');
    printf("Total counting is %d", cnt);
    return 0;
}
