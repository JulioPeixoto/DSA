#include <iostream>
using namespace std;

class Node {

public:
    int value;
    Node *next;
    Node *previous;
};

void printForward(Node *head) {
    Node *traverse = head;
    while (traverse != nullptr) {
    
        cout << traverse->value << endl;
        traverse = traverse->next;
    }
}

void printBackward(Node *tail) {
    Node *traverse = tail;
    while (traverse != nullptr) {
    
        cout << traverse->value << endl;
        traverse = traverse->previous;
    }
}

void insertAtBeginning(Node *&head, int value) {
    Node *newNode = new Node;
    newNode->value = value;
    newNode->next = head;
    newNode->previous = nullptr;
    if (head != nullptr) {
        head->previous = newNode;
    }
    head = newNode;
}

void insertAtEnd(Node *&tail, int value) {
    
    Node *newNode = new Node;
    newNode->value = value;
    newNode->next = nullptr;
    newNode->previous = tail;
    if (tail != nullptr) {
        tail->next = newNode;
    }
    tail = newNode;
}

void removeNode(Node *&head, Node *&tail, int value) {

    Node *current = head;
    while (current != nullptr) {
        if (current->value == value) {
            if (current->previous != nullptr) {
                current->previous->next = current->next;
            }
            else {
                head = current->next;
            }
            if (current->next != nullptr) {   
                current->next->previous = current->previous;
            }
            else {
            
                tail = current->previous;
            }
            delete current;
            return;
        }
        current = current->next;
    }
}

void clearList(Node *head, Node *tail) {
    while (head != nullptr) {
        Node *current = head;
        head = current->next;
        delete current;
    }
    tail = nullptr;
}

bool existData(Node *head, int value) {
    Node *current = head;
    while (current != nullptr) {
        if (current->value == value){
            return true;
        }
        current = current->next;
    }
    return false;
}

int getSize(Node *head) {
    int c = 0;
    Node *current = head;
    while (current != nullptr) {
        c++;
        current = current->next;
    }
    return c;
}

int main() {
    Node *head;
    Node *tail;

    Node *node = new Node();
    node->value = 4;
    node->next = nullptr;
    node->previous = nullptr;
    head = node;
    tail = node;

    node = new Node();
    node->value = 5;
    node->next = nullptr;
    node->previous = tail;
    tail->next = node;
    tail = node;

    int t = 55;

    insertAtBeginning(head, 99);
    insertAtEnd(tail, 55);
    printForward(head);
    bool a = existData(head, t);
    std::cout<< a << endl;
    int size = getSize(head);
    std::cout<< "Size = " << size << endl;
    clearList(head, tail);
    
    
    
    return 0;
}