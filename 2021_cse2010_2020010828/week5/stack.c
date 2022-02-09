#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0

//stack구조체 선언 (linked list)
typedef struct StackNode {
	int data;
	struct StackNode* next;
} StackNode;

//stack관련 함수
void pushLinkedStack(StackNode** top, int data);
StackNode* popLinkedStack(StackNode** top);
StackNode* topLinkedStack(StackNode* top);
void deleteLinkedStack(StackNode** top);

int isEmpty(StackNode* top) {
	if (top == NULL)
		return TRUE;
	else
		return FALSE;
}

void pushLinkedStack(StackNode** top, int data) {
	StackNode* pnode;
	pnode = (StackNode*)malloc(sizeof(StackNode));
	pnode->data = data;
	pnode->next = NULL;

	if (isEmpty(*top)) {
		*top = pnode;
	}
	else {
		pnode->next = *top;
		*top = pnode;
	}
}

StackNode* popLinkedStack(StackNode** top) {
	StackNode* pnode = NULL;

	if (isEmpty(*top)) {
		printf("Nothing! Error\n");
		return NULL;
	}
	pnode = *top;
	*top = pnode->next;
	

	return pnode;
}

StackNode* topLinkedStack(StackNode* top) {
	StackNode* pnode = NULL;

	if (!isEmpty(top)) {
		pnode = top;
	}
	return pnode;
}

void deleteLinkedStack(StackNode** top) {
	StackNode* pnode = NULL, * pDelNode = NULL;
	pnode = *top;
	while (pnode != NULL) {
		pDelNode = pnode;
		pnode = pnode->next;
		free(pDelNode);
	}
	*top = NULL;
}

void showLInkedStack(StackNode* top) {
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

int main() {
	//가장 윗 부분을 가리키는 top 포인터 선언

	StackNode* top = NULL;
	StackNode* pNode;

	printf("Push 10, 20, 30 called.\n");
	pushLinkedStack(&top, 10);
	pushLinkedStack(&top, 20);
	pushLinkedStack(&top, 30);
	showLInkedStack(top);

	printf("Pop() called.\n");
	pNode = popLinkedStack(&top);
	if (pNode) {
		free(pNode);
		showLInkedStack(top);
	}

	printf("Top() called.\n");
	pNode = topLinkedStack(top);
	if (pNode)
		printf("Top node's data: %d\n", pNode->data);
	else
		printf("The stack is empty.\n");
	showLInkedStack(top);

	deleteLinkedStack(&top);

	return 0;
}
