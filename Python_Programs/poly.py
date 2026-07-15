class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coeff, power):
        new_node = Node(coeff, power)

   
        if self.head is None or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        while temp.next and temp.next.power > power:
            temp = temp.next

   
        if temp.next and temp.next.power == power:
            temp.next.coeff += coeff
        elif temp.power == power:
            temp.coeff += coeff
        else:
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        if self.head is None:
            print("0")
            return

        temp = self.head
        while temp:
            print(f"{temp.coeff}x^{temp.power}", end="")
            if temp.next:
                print(" + ", end="")
            temp = temp.next
        print()


def add(poly1, poly2):
    p = poly1.head
    q = poly2.head
    result = Polynomial()

   
    while p and q:
        if p.power == q.power:
            result.insert(p.coeff + q.coeff, p.power)
            p = p.next
            q = q.next

        elif p.power > q.power:
            result.insert(p.coeff, p.power)
            p = p.next

        else:
            result.insert(q.coeff, q.power)
            q = q.next

    while p:
        result.insert(p.coeff, p.power)
        p = p.next

    while q:
        result.insert(q.coeff, q.power)
        q = q.next

    return result



poly1 = Polynomial()
poly2 = Polynomial()

n1 = int(input("Enter number of terms in first polynomial: "))
print("Enter coefficient and power (in descending order of powers):")

for i in range(n1):
    c = int(input("Coefficient: "))
    p = int(input("Power: "))
    poly1.insert(c, p)

n2 = int(input("\nEnter number of terms in second polynomial: "))
print("Enter coefficient and power (in descending order of powers):")

for i in range(n2):
    c = int(input("Coefficient: "))
    p = int(input("Power: "))
    poly2.insert(c, p)

print("\nFirst Polynomial:")
poly1.display()

print("Second Polynomial:")
poly2.display()

sum_poly = add(poly1, poly2)

print("Sum Polynomial:")
sum_poly.display()