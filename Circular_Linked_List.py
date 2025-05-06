class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self, elements):
        for element in elements:
            self.insert_at_end(element)

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head == None:
            print("Linked List is Empty!")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("[Head]")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        new_node.next = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        self.head = new_node

    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return

        temp = self.head
        cnt = 0
        while temp.next != self.head and cnt < pos - 1:
            temp = temp.next
            cnt += 1
        if temp.next == self.head:
            temp.next = new_node
            new_node.next = self.head
        else:
            new_node.next = temp.next
            temp.next = new_node

    def delete_node(self, pos):
        if self.head.next == self.head:
            self.head = None
        elif pos == 0:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_head = self.head.next
            temp.next = new_head
            self.head = new_head
        else:
            temp = self.head
            cnt = 0
            while temp.next != self.head and cnt < pos - 1:
                temp = temp.next
                cnt += 1
            temp.next = temp.next.next
    def count(self):
        if self.head == None:
            print("Linked List is empty!")
            return

        if self.head.next == self.head:
            print("Length of the Linked list is:", 1)
            return
        else:
            cnt = 1
            temp = self.head
            while temp.next != self.head:
                cnt += 1
                temp = temp.next

        print("Length of the Linked list is:", cnt)

    def max(self):
        if self.head == None:
            print("Linked List is empty!")
            return
        maxx = self.head.data
        temp = self.head
        while temp.next != self.head:
            if temp.data > maxx:
                maxx = temp.data
            temp = temp.next
        if temp.data > maxx:
            maxx = temp.data

        print("Maximum element:", maxx)

    def min(self):
        if self.head == None:
            print("Linked List is empty!")
            return
        min = self.head.data
        temp = self.head
        while temp.next != self.head:
            if temp.data < min:
                min = temp.data
            temp = temp.next
        if temp.data < min:
            min = temp.data

        print("Minimum element:", min)

    def sum_of_element(self):
        temp = self.head
        summ = 0
        while temp.next != self.head:
            summ += temp.data
            temp = temp.next

        summ += temp.data
        print("Sum of the elements is:", summ)


def menu():
    cll = CircularLinkedList()
    while True:
        print("\nMenu:")
        print("1. Create list")
        print("2. Display list")
        print("3. Insert at beginning")
        print("4. Insert at end")
        print("5. Insert at given position")
        print("6. Insert at right postion")
        print("7. Insert at left postion")
        print("8. Delete node by position")
        print("9. Sum of elements")
        print("10. Maximum element")
        print("11. Minimum element")
        print("12. Length of the Linked List")
        print("13. Exit")
        print()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = list(
                map(int, input("Enter elements separated by space: ").split())
            )
            cll.create(elements)
        elif choice == 2:
            cll.display()
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            cll.insert_at_beginning(data)
        elif choice == 4:
            data = int(input("Enter data to insert: "))
            cll.insert_at_end(data)
        elif choice == 5:
            data = int(input("Enter data to insert: "))
            pos = int(input("Enter the index: "))
            cll.insert_at_pos(data, pos)
        elif choice == 6:
            data = int(input("Enter data to whose next to insert: "))
            pos = int(input("Enter the data to insert: "))
            cll.append_right_node(data, pos)
        elif choice == 7:
            data = int(input("Enter data to whose prev to insert: "))
            pos = int(input("Enter the data to insert: "))
            cll.append_left_node(data, pos)
        elif choice == 8:
            index = int(input("Enter the index to delete: "))
            cll.delete_node(index)
        elif choice == 9:
            cll.sum_of_element()
        elif choice == 10:
            cll.max()
        elif choice == 11:
            cll.min()
        elif choice == 12:
            cll.count()
        elif choice == 13:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
