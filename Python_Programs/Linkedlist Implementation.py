class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        print(data, "added to stack")

    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            print("Removed:", temp.data)
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Top Element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            print("Stack Elements:")
            while temp:
                print(temp.data)
                temp = temp.next

s = Stack()

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        item = input("Enter Book Title: ")
        s.push(item)
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.peek()
    elif ch == 4:
        s.display()
    elif ch == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")

