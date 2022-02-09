#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* leftchild;
    struct Node* rightchild;
}Node;

void insertTreeNode(Node** p, int value);
void printTreePreOrder(Node* pNode);
void printTreePostOrder(Node* pNode);
void printTreeInOrder(Node* pNode);

void insertTreeNode(Node** p, int value) {

    if ((*p) == NULL) {
        (*p) = (Node*)malloc(sizeof(Node));
        (*p)->data = value;
        (*p)->leftchild = NULL;
        (*p)->rightchild = NULL;
    }
    else if ((*p)->data > value) {
        insertTreeNode(&((*p)->leftchild), value);
    }
    else {
        insertTreeNode(&((*p)->rightchild), value);
    }
}

void printTreePreOrder(Node* pNode) {
    if (pNode == NULL) {
        return;
    }

    printf("%3d ", pNode->data);
    printTreePreOrder(pNode->leftchild);
    printTreePreOrder(pNode->rightchild);
}

void printTreePostOrder(Node* pNode) {
    if (pNode == NULL) {
        return;
    }

    printTreePostOrder(pNode->leftchild);
    printTreePostOrder(pNode->rightchild);
    printf("%3d ", pNode->data);

}

void printTreeInOrder(Node* pNode) {
    if (pNode == NULL) {
        return;
    }

    printTreeInOrder(pNode->leftchild);
    printf("%3d ", pNode->data);
    printTreeInOrder(pNode->rightchild);


}





int main() {
    Node* pParentNode = NULL;

    insertTreeNode(&pParentNode, 4);
    insertTreeNode(&pParentNode, 2);
    insertTreeNode(&pParentNode, 6);
    insertTreeNode(&pParentNode, 1);
    insertTreeNode(&pParentNode, 3);
    insertTreeNode(&pParentNode, 5);
    insertTreeNode(&pParentNode, 7);

    printf("Preorder : \n");
    printTreePreOrder(pParentNode);
    printf("\nInorder: \n");
    printTreeInOrder(pParentNode);
    printf("\nPostOrder: \n");
    printTreePostOrder(pParentNode);

    printf("\n");

    return 0;
}