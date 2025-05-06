#Single Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def create(self, elements):
        for element in elements:
            self.insert_at_end(element)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print("Node not found.")
            return
        prev.next = temp.next
        temp = None
    def delete_first_node(self, data):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
        else:
            print("List is empty.")
    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        current = self.head
        for i in range(position - 1):
            if current == None:
                print("Position out of bounds")
            current = current.next
        if current == None:
            print("Position out of bounds")
        new_node.next = current.next
        current.next = new_node
    def sum(self):
        current = self.head
        sum = 0
        while current:
            sum += current.data
            current = current.next
        return sum
    def insert_at_next_to_data(self, target_data, newdata):
        new_node = Node(newdata)
        temp = self.head
        while temp:
            if temp.data == target_data:
                break
            temp = temp.next
        if temp == None:
            print("Insertion is not possible")
        new_node.next = temp.next
        temp.next = new_node
    def insert_at_left_of_data(self, data, node_previous):
        new_node = Node(data)
        current = self.head
        node_previous = None
        while current:
            if current.data == node_previous:
                break
            node_previous = current
            current = current.next
        if current is None:
            print("Insertion is not possible")
        new_node.next = current
        node_previous.next = new_node
    def count_even_odd_nodes(self):
        temp = self.head
        even_count = odd_count = 0
        while temp:
            if temp.data % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            temp = temp.next
        print(f"Number of even nodes: {even_count}")
        print(f"Number of odd nodes: {odd_count}")
    def reverse_linked_list(self):
        p = self.head
        r = None
        while p:
            q = p
            p = p.next
            q.next = r
            r = q
        self.head = q
    def maximum_element(self):
        temp = self.head
        maximum = temp.data
        while temp:
            if temp.data > maximum:
                maximum = temp.data
            temp = temp.next
        return maximum
    def minimum_element(self):
        temp = self.head
        minimum = temp.data
        while temp:
            if temp.data < minimum:
                minimum = temp.data
            temp = temp.next
        return minimum
    def count(self):
        c = 0
        temp = self.head
        while temp:
            c = c + 1
            temp = temp.next
        return c
    def display(self):
        if self.head == None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def menu():
    sll = SinglyLinkedList()
    while True:
        print("\nMenu:")
        print("1. Create list")
        print("2. Display list")
        print("3. Insert at beginning")
        print("4. Insert at end")
        print("5. Delete a node")
        print("6. Delete first node")
        print("7. Insert at position")
        print("8. Find sum")
        print("9. Insert at right next to data")
        print("10. Insert at left before data")
        print("11. Count Even and Odd nodes")
        print("12. Reverse linked list")
        print("13. Find maximum data")
        print("14. Find minimum data")
        print("15. Count number of elements")
        print("16. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            sll.create(elements)
        elif choice == 2:
            sll.display()
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            sll.insert_at_beginning(data)
        elif choice == 4:
            data = int(input("Enter data to insert: "))
            sll.insert_at_end(data)
        elif choice == 5:
            key = int(input("Enter the node to delete: "))
            sll.delete_node(key)
        elif choice == 6:
            data = int(input("Enter data to delete: "))
            sll.delete_first_node(data)
        elif choice == 7:
            position = int(input("Enter position to insert: "))
            data = int(input("Enter data to insert: "))
            sll.insert_at_position(position, data)
        elif choice == 8:
            sll.sum()
            print(f"Sum: {sll.sum()}")
        elif choice == 9:
            target_data = int(input("Enter data to insert new data: "))
            newdata = int(input("Enter new data to insert: "))
            sll.insert_at_next_to_data(target_data, newdata)
        elif choice == 10:
            node_previous = int(input("Enter previous node to insert: "))
            data = int(input("Enter data to insert new data: "))
            sll.insert_at_left_of_data(data, node_previous)
        elif choice == 11:
            sll.count_even_odd_nodes()
        elif choice == 12:
            sll.reverse_linked_list()
        elif choice == 13:
            sll.maximum_element()
            print("Maximum data in the linked list: ", sll.maximum_element())
        elif choice == 14:
            sll.minimum_element()
            print("Minimum data in the linked list: ", sll.minimum_element())
        elif choice == 15:
            sll.count()
            print("Number of elements in the linked list: ", sll.count())
        elif choice == 16:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
