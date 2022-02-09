#include <stdio.h>
#include <malloc.h>
#define TRUE 1;
#define FALSE -1;
typedef struct node {
    int data;
    struct node* nextNode;
}Node;

typedef struct StackNode {
    int data;
    struct StackNode* next;
} StackNode;

int isEmpty(StackNode* top) {
    if (top == NULL) {
        return TRUE;
    }
    else {
        return FALSE;
    }

}

typedef struct LinkedList {
    int curcount;  // 총 list에 들어있는 node의 개수
    Node headNode; // list의 시작 node
}LinkedList;

StackNode* popLinkedStack(StackNode** top) {
    StackNode* pNode = NULL;

    if (isEmpty(*top) == 1) {
        printf("Nothing~\n");
        return NULL;
    }
    pNode = *top;
    *top = pNode->next;

    return pNode;
}

void pushLinkedStack(StackNode** top, int data) {
    StackNode* pNode = NULL;
    pNode = (StackNode*)malloc(sizeof(StackNode));
    pNode->data = data;
    pNode->next = NULL;

    if (isEmpty(*top) == 1) {
        (*top) = pNode;
        return;
    }
    else {
        pNode->next = (*top);
        (*top) = pNode;
    }

}
// Use this to find out whether there is remainings.
void showLinkedStack(StackNode* top) {
    StackNode* pNode = NULL;
    if (isEmpty(top)) {
        printf("the stack is empty\n");
        return;
    }

    pNode = top;
    printf("==============Show Stack===============\n");
    while (pNode != NULL) {
        printf("[%d]\n", pNode->data);
        pNode = pNode->next;
    }
    printf("=======================================\n");
}

void addnode(LinkedList* p, int a, int num) {
    Node* tmpNode;
    Node* newNode;
    newNode = malloc(sizeof(Node));

    // 예외
    if (p == NULL) return;

    // 템프 노드는 헤드가 가르키는 노드를 가르킴
    tmpNode = p->headNode.nextNode;
    newNode->nextNode = NULL;
    newNode->data = num;
    if (a > p->curcount) return;
    //TODO
    if (a == 0 && tmpNode == NULL) {
        p->headNode.nextNode = newNode;
        /*
        if(tmpNode->nextNode == NULL){
            (p->curcount)++;
            return;
        }

        newNode->nextNode = tmpNode->nextNode;
         */
    }
    else {

        for (int i = 0; i < a - 1; i++) {
            tmpNode = tmpNode->nextNode;
        }
        newNode->nextNode = tmpNode->nextNode;
        tmpNode->nextNode = newNode;
    }
    (p->curcount)++;
}
void makeEmpty(LinkedList* p) {
    Node* tmpNode, * deleteNode;

    tmpNode = p->headNode.nextNode;
    if (tmpNode == NULL) {
        return;
    }

    while (tmpNode != NULL) {
        (p->curcount)--;
        deleteNode = tmpNode;
        tmpNode = tmpNode->nextNode;
        free(deleteNode);
    }
    // 맨마지막에 이렇게 넣어준다.
    p->headNode.nextNode = NULL;


}

void shownode(LinkedList* p) {
    Node* tmpNode;
    tmpNode = p->headNode.nextNode;
    printf("현재 Node 개수: %d\n", p->curcount);
    if (tmpNode == NULL) {
        return;
    }


    while (tmpNode != NULL) {
        printf("[%d]\n", tmpNode->data);
        tmpNode = tmpNode->nextNode;
    }
}

void reverseList(LinkedList* p, StackNode** top) {
    // Node *tmpnode;
    int cnt = 0;
    StackNode* tmpstack;
    tmpstack = (StackNode*)malloc(sizeof(StackNode));
    while (p->headNode.nextNode != NULL) {
        pushLinkedStack(top, p->headNode.nextNode->data);
        p->headNode.nextNode = p->headNode.nextNode->nextNode;
    }
    makeEmpty(p);
    while (isEmpty(*top) != 1) {
        tmpstack = popLinkedStack(top);
        addnode(p, cnt, tmpstack->data);
        (p->curcount)--;
        cnt++;
    }
}



int main() {

    LinkedList* linkedList = (LinkedList*)malloc(sizeof(LinkedList));
    linkedList->curcount = 0;
    linkedList->headNode.nextNode = NULL;

    StackNode* top = NULL;
    // StackNode* pNode;
    addnode(linkedList, 0, 10);
    addnode(linkedList, 5, 100);
    addnode(linkedList, 1, 20);
    addnode(linkedList, 2, 30);
    addnode(linkedList, 1, 50);
    addnode(linkedList, 1, 70);
    addnode(linkedList, 1, 40);

    shownode(linkedList);

    reverseList(linkedList, &top);
    //  showLinkedStack(top);
    shownode(linkedList);

    makeEmpty(linkedList);
    shownode(linkedList);

    return 0;
}