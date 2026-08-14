import sys

class Stack:
    # Constructor: used to create memory
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.mystack = []  # list is used to implement stack in Python

    # Check whether stack is full
    def isFull(self):
        if len(self.mystack) == self.stackSize:
            return True
        else:
            return False

    # Push element into stack
    def push(self, value):
        if self.isFull():
            print("Stack is full")
        else:
            self.mystack.append(value)
            print("Element pushed:", value)

    # Check whether stack is empty
    def isEmpty(self):
        if self.mystack == []:
            return True
        else:
            return False

    # Remove top element
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Element popped:", self.mystack.pop())

    # Display top element
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element =", self.mystack[-1])

    # Delete stack
    def deleteStack(self):
        self.mystack = None
        print("Stack is deleted")

    # Display stack
    def display(self):
        if self.mystack is None:
            print("Stack is deleted")
        elif self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack:", self.mystack)


# Take stack size from user
size = int(input("Enter the size of the stack: "))

# Create object of class
obj = Stack(size)

# Menu
while True:
    print("\n1. Push element")
    print("2. Pop element")
    print("3. Peek element")
    print("4. IsEmpty")
    print("5. IsFull")
    print("6. Delete Stack")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to push in stack: "))
        obj.push(value)

    elif choice == 2:
        obj.pop()

    elif choice == 3:
        obj.peek()

    elif choice == 4:
        print("Is Empty:", obj.isEmpty())

    elif choice == 5:
        print("Is Full:", obj.isFull())

    elif choice == 6:
        obj.deleteStack()

    elif choice == 7:
        obj.display()

    elif choice == 8:
        print("Program ended")
        sys.exit()

    else:
        print("Invalid choice")