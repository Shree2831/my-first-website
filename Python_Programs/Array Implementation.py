class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self):
        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            item = input("Enter Book Title: ")
            self.stack.append(item)
            print(item, "added to stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Removed:", self.stack.pop())

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top Element:", self.stack[-1])

    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack Elements:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])

size = int(input("Enter Stack Size: "))
s = Stack(size)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        s.push()
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.peek()
    elif ch == 4:
        s.display()
    elif ch == 5:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")

