#define TESTCASE_PATH "testCases.txt"
#define BUFFSIZE 1024
#define _CRT_SECURE_NO_WARNINGS
#include "stdlib.h"
#include "stdio.h"
#include "string.h"

typedef struct polyTerm_ {
    int exp;
    int coeff;
    struct polyTerm_* next;
} polyTerm;

typedef struct poly_ {
    polyTerm* head;
} poly;

void initPoly(poly* A) {
    A->head = NULL;
}

void clearPoly(poly* A) {
    polyTerm* tmpPoly;
    tmpPoly = A->head;
    while (tmpPoly != NULL) {
        A->head = tmpPoly->next;
        tmpPoly = A->head;
    }

}

void printPoly_impl(poly A, char* buffer) {
    polyTerm* tmpnode;
    tmpnode = A.head;
    int first = 1;
    while (tmpnode) {
        if (tmpnode->coeff == 0) {
            tmpnode = tmpnode->next;
            continue;
        }
        else if (tmpnode->coeff > 0 && first == 0) {
            printf("+");
        }
        first = 0;
        printf("%dx^%d", tmpnode->coeff, tmpnode->exp);
        tmpnode = tmpnode->next;

    }

    printf("\n");
}

void printPoly(poly A) {
    char buffer[BUFFSIZE] = "";
    if (A.head == NULL) {
        printf("Nothing in this polynomial\n");
    }
    printPoly_impl(A, buffer);
    printf(buffer);
}

void addTerm(poly* A, int exp, int coeff) {
    polyTerm* temp;
    polyTerm* newnode;
    newnode = (polyTerm*)malloc(sizeof(polyTerm));

    newnode->coeff = coeff;
    newnode->exp = exp;
    newnode->next = NULL;
    if (A->head == NULL) {
        A->head = newnode;
        return;
    }
    temp = A->head;
    while (temp->next) {
        temp = temp->next;
    }
    temp->next = newnode;
    // free(newnode);
}

poly multiPoly(poly A, poly B) {
    polyTerm* Atemp;
    polyTerm* Btemp;
    int expon, coef;

    polyTerm* temp;
    poly Result;
    int max = 0;
    poly Temp;

    Temp.head = NULL;
    Result.head = NULL;

    Btemp = B.head;
    while (Btemp) {
        Atemp = A.head;
        while (Atemp) {
            expon = Btemp->exp + Atemp->exp;
            coef = Btemp->coeff * Atemp->coeff;

            addTerm(&Temp, expon, coef);
            Atemp = Atemp->next;
        }
        Btemp = Btemp->next;
    }
    // 오름차순으로 바꾸는 코드
    temp = Temp.head;
    temp->next = Temp.head->next;
    while (temp) {
        if (temp->exp > max) {
            max = temp->exp;
        }
        temp = temp->next;
    }
    int* array;
    array = malloc(sizeof(int) * (max + 1));
    for (int i = 0; i <= max; i++) {
        temp = Temp.head;
        array[i] = 0;
        while (temp) {
            if (temp->exp == max - i) {
                *(array + i) += temp->coeff;

            }
            temp = temp->next;
        }
    }
    for (int i = 0; i <= max; i++) {
        addTerm(&Result, max - i, array[i]);
    }
    free(array);
    return Result;

}

void testPoly() { //You don't have to use this func.
    int breakFlag = 0;
    int breakPoint = -1;
    FILE* fp = fopen(TESTCASE_PATH, "r");
    poly A, B;
    initPoly(&A);
    initPoly(&B);
    printf("===\n");
    int T;
    fscanf(fp, "%d\n", &T);

    char lastTrue[BUFFSIZE] = "";
    char lastAnswer[BUFFSIZE] = "";

    while (T--) {
        char inputOp0, inputOp1;
        char inputStr[BUFFSIZE] = "";
        char buffer[BUFFSIZE] = "";
        int caseNum;

        fscanf(fp, "%d %c ", &caseNum, &inputOp0);

        if (inputOp0 == 'a') {
            int exp, coeff;
            fscanf(fp, "%c %d %d\n", &inputOp1, &exp, &coeff);
            if (inputOp1 == 'A') {
                addTerm(&A, exp, coeff);
            }
            else if (inputOp1 == 'B') {
                addTerm(&B, exp, coeff);
            }
        }

        else if (inputOp0 == 'p') {
            fscanf(fp, "%c\n%s\n", &inputOp1, inputStr);
            if (inputOp1 == 'A') {
                printPoly_impl(A, buffer);
            }
            else if (inputOp1 == 'B') {
                printPoly_impl(B, buffer);
            }

            if (strcmp(inputStr, buffer) != 0) {
                breakFlag = 1;
                breakPoint = caseNum;
                strcpy(lastTrue, inputStr);
                strcpy(lastAnswer, buffer);
                break;
            }
        }

        else if (inputOp0 == 'c') {
            fscanf(fp, "%c\n", &inputOp1);
            if (inputOp1 == 'A') {
                clearPoly(&A);
            }
            else if (inputOp1 == 'B') {
                clearPoly(&B);
            }
        }

        else if (inputOp0 == 'm') {
            fscanf(fp, "%s\n", inputStr);
            printPoly_impl(multiPoly(A, B), buffer);
            if (strcmp(inputStr, buffer) != 0) {
                breakFlag = 1;
                breakPoint = caseNum;
                strcpy(lastTrue, inputStr);
                strcpy(lastAnswer, buffer);
                break;
            }
        }
    }

    fclose(fp);

    if (breakFlag) {
        printf("Test failed on case# %d\n", breakPoint);
        printf("True: %s\nAnswer: %s", lastTrue, lastAnswer);
    }
    else {
        printf("TEST DONE.\n");
    }
}

int main() {
    // testPoly(); //use this function if you want.

    poly A, B;
    initPoly(&A);
    initPoly(&B);

    addTerm(&A, 1, 1);
    addTerm(&A, 0, 1);
    printf("poly A: ");
    printPoly(A);
    printf("\n");

    addTerm(&B, 1, 1);
    addTerm(&B, 0, -1);
    printf("poly B: ");
    printPoly(B);
    printf("\n");

    printf("A*B: ");
    printPoly(multiPoly(A, B));

    //Check whether linkedlist polynomial is safely deleted completely! 
    clearPoly(&A);
    clearPoly(&B);

    printPoly(A);
    printPoly(B);
    return 0;
}