# import sys

# class Queue:
#     # Constructor: used to create memory
#     def __init__(self, queueSize):
#         self.queueSize = queueSize
#         self.mylist = []  # list is used to implement queue in Python

#     # Check whether queue is full
#     def isFull(self):
#         if len(self.mylist) == self.queueSize:
#             return True
#         else:
#             return False

#     # Insert element into queue
#     def enqueue(self, value):
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.mylist.append(value)
#             print("Element inserted:", value)

#     # Check whether queue is empty
#     def isEmpty(self):
#         if self.mylist == []:
#             return True
#         else:
#             return False

#     # Remove element from queue
#     def dequeue(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print("Element removed:", self.mylist.pop(0))

#     # Display front element
#     def peek(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print("Front element =", self.mylist[0])

#     # Delete queue
#     def deleteQueue(self):
#         self.mylist = None
#         print("Queue is deleted")

#     # Display queue
#     def display(self):
#         if self.mylist is None:
#             print("Queue is deleted")
#         elif self.isEmpty():
#             print("Queue is empty")
#         else:
#             print("Queue:", self.mylist)


# # Take queue size from user
# size = int(input("Enter the size of the queue: "))

# # Create object of class
# obj = Queue(size)

# # Menu
# while True:
#     print("\n1. Enqueue element")
#     print("2. Dequeue element")
#     print("3. Peek element")
#     print("4. IsEmpty")
#     print("5. IsFull")
#     print("6. Delete Queue")
#     print("7. Display")
#     print("8. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter the value to insert in queue: "))
#         obj.enqueue(value)

#     elif choice == 2:
#         obj.dequeue()

#     elif choice == 3:
#         obj.peek()

#     elif choice == 4:
#         print("Is Empty:", obj.isEmpty())

#     elif choice == 5:
#         print("Is Full:", obj.isFull())

#     elif choice == 6:
#         obj.deleteQueue()

#     elif choice == 7:
#         obj.display()

#     elif choice == 8:
#         print("Program ended")
#         sys.exit()

#     else:
#         print("Invalid choice")


class Student:
    def __init__(self, rollno):
        self.rollno = rollno

    def displayRollno(self):
        print(self.rollno)


obj1 = Student(101)
obj2 = Student(102)
obj3 = Student(103)

obj1.displayRollno()
obj2.displayRollno()
obj3.displayRollno()

obj1.rollno = 111
obj1.displayRollno()
obj2.displayRollno()
obj3.displayRollno()

class College:
    collegename = "Modern College"  # static/class variable

    def __init__(self):
        self.studentname = "prashant"  # instance variable


principal = College()
teacher = College()
accountant = College()

print("principal =", principal.collegename, "....", principal.studentname)
print("teacher   =", teacher.collegename, "....", teacher.studentname)
print("accountant =", accountant.collegename, "....", accountant.studentname)

College.collegename = "HBD"

principal.studentname = "prashant jha"

print("principal =", principal.collegename, "|", principal.studentname)
print("teacher   =", teacher.collegename, "|", teacher.studentname)
print("accountant =", accountant.collegename, "|", accountant.studentname)