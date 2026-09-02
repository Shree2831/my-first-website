class Node:
    def __init__(self, enrollment_id, student_name, course):
        self.enrollment_id = enrollment_id
        self.student_name = student_name
        self.course = course
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    
    def right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))
        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        return x

   
    def left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

   
    def insert(self, root, enrollment_id, student_name, course):

        if root is None:
            return Node(enrollment_id, student_name, course)

        if enrollment_id < root.enrollment_id:
            root.left = self.insert(root.left, enrollment_id,
                                     student_name, course)

        elif enrollment_id > root.enrollment_id:
            root.right = self.insert(root.right, enrollment_id,
                                      student_name, course)

        else:
            print("Enrollment ID already exists!")
            return root

        
        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

       
        balance = self.get_balance(root)

        
        if balance > 1 and enrollment_id < root.left.enrollment_id:
            return self.right_rotate(root)

       
        if balance < -1 and enrollment_id > root.right.enrollment_id:
            return self.left_rotate(root)

        if balance > 1 and enrollment_id > root.left.enrollment_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and enrollment_id < root.right.enrollment_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    
    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    
    def delete(self, root, enrollment_id):

        if root is None:
            return root

        if enrollment_id < root.enrollment_id:
            root.left = self.delete(root.left, enrollment_id)

        elif enrollment_id > root.enrollment_id:
            root.right = self.delete(root.right, enrollment_id)

        else:
           
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            
            temp = self.min_value_node(root.right)

            root.enrollment_id = temp.enrollment_id
            root.student_name = temp.student_name
            root.course = temp.course

            root.right = self.delete(root.right, temp.enrollment_id)

        
        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        
        balance = self.get_balance(root)

        
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

       
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, enrollment_id):

        if root is None:
            return None

        if enrollment_id == root.enrollment_id:
            return root

        if enrollment_id < root.enrollment_id:
            return self.search(root.left, enrollment_id)

        return self.search(root.right, enrollment_id)

   
    def inorder(self, root):

        if root:
            self.inorder(root.left)

            print("Enrollment ID:", root.enrollment_id,
                  "| Student Name:", root.student_name,
                  "| Course:", root.course)

            self.inorder(root.right)

    
    def count(self, root):

        if root is None:
            return 0

        return 1 + self.count(root.left) + self.count(root.right)



avl = AVLTree()
root = None

while True:

    print("\n===== STUDENT ENROLLMENT AVL TREE =====")
    print("1. Insert an Enrollment Record")
    print("2. Delete a Record by Enrollment ID")
    print("3. Search for a Student Enrollment")
    print("4. Display All Enrollments (Sorted)")
    print("5. Count Total Enrollments")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

   
    if choice == 1:

        enrollment_id = int(input("Enter Enrollment ID: "))
        student_name = input("Enter Student Name: ")
        course = input("Enter Course: ")

        root = avl.insert(root, enrollment_id,
                           student_name, course)

        print("Enrollment record inserted successfully!")

   
    elif choice == 2:

        enrollment_id = int(input("Enter Enrollment ID to delete: "))

        if avl.search(root, enrollment_id):
            root = avl.delete(root, enrollment_id)
            print("Enrollment record deleted successfully!")
        else:
            print("Enrollment ID not found!")

  
    elif choice == 3:

        enrollment_id = int(input("Enter Enrollment ID to search: "))

        result = avl.search(root, enrollment_id)

        if result:
            print("\nEnrollment Found!")
            print("Enrollment ID:", result.enrollment_id)
            print("Student Name:", result.student_name)
            print("Course:", result.course)
        else:
            print("Enrollment ID not found!")

    
    elif choice == 4:

        if root is None:
            print("No enrollment records available!")
        else:
            print("\nEnrollment Records (Sorted by Enrollment ID):")
            avl.inorder(root)

    
    elif choice == 5:

        total = avl.count(root)
        print("Total Enrollment Records:", total)

   
    elif choice == 6:
        print("Program exited successfully!")
        break

    else:
        print("Invalid choice! Please try again.")
