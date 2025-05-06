class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def create(self,elements):
        for element in elements:
            self.append(element)
    def append(self, data):
        if self.head is None:
            new_node = Node(data)            
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
    def append_at_position(self, position, element):
        new_node = Node(element)
        if position == 0:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for i in range(position-1):
                if current is None:
                    print("Position out of range")
                current = current.next
            if current is None:
                print("Position out of range")
            else:
                new_node.next = current.next
                current.next = new_node
                new_node.prev = current
                new_node.next.prev = new_node
    def append_right_to_node(self, data,new_data):
        current = self.head
        while current:
            if current.data == data:
                break
            current = current.next
        if current is None:
            print("Insertion is not possible")
        else:
            new_node = Node(new_data)
            new_node.prev = current
            new_node.next = current.next
            current.next = new_node
            new_node.next.prev = new_node
    def append_left_to_node(self, data,new_data):
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == data:
                break
            current = current.next
        if current is None:
            print("Insertion is not possible")
        else:
            new_node.prev = current.prev
            new_node.next = current
            current.prev = new_node
            current.prev.next = new_node
    def delete_node(self, data):
        current = self.head
        if current is None:
            print("Deletion is not possible")
            return
        if self.head.data == data:
            self.head = self.head.next
            current = None
        else:
            current = self.head.next
            while current:
                if current.data == data:
                    break
                else:
                    current = current.next
            if current is None:
                print("Deletion is not possible")
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                current = None
    def delete_first_node(self):
        current = self.head
        if current is not None:
            self.head = current.next
            current = None
        else:
            print("List is empty")
    def delete_last_node(self):
        current = self.head
        if current is None:
            print("Deletion is not possible")
            return
        while current:
            if current.next == None:
                current.prev.next = current.next
                current = None
            else:
                current = current.next
    def sum_of_elements(self):
        current = self.head
        sum = 0
        while current:
            sum += current.data
            current = current.next
        return sum
    def max_elements(self):
        current = self.head
        max_value = current.data
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value
    def min_elements(self):
        current = self.head
        min_value = current.data
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value
    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data,end = "->")
            current = current.next
        print("None")
def menu():
    dll = DoubleLinkedList()
    while True:
        print("\nMenu:")
        print("1. Create list")
        print("2. Display list")
        print("3. Insert at beginning")
        print("4. Insert at end")
        print("5. Insert at position")
        print("6. Insert at right after to data")
        print("7. Insert at left before data")
        print("8. Delete a node ")
        print("9. Delete first node")
        print("10.Delete last node")
        print("11. Find sum")
        print("12. Find maximum data")
        print("13. Find minimum data")
        print("14. Count number of elements")
        print("15. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            dll.create(elements)
        elif choice == 2:
            dll.display()
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            dll.prepend(data)
        elif choice == 4:
            data = int(input("Enter data to insert: "))
            dll.append(data)
        elif choice == 5:
            position = int(input("Enter position to insert: "))
            data = int(input("Enter data to insert: "))
            dll.append_at_position(position, data)
        elif choice == 6:
            target_data = int(input("Enter data to insert new data: "))
            new_data = int(input("Enter new data: "))
            dll.append_right_to_node(target_data, new_data)
        elif choice == 7:
            target_data = int(input("Enter previous node to insert: "))
            new_data = int(input("Enter data to insert new data: "))
            dll.append_left_to_node(target_data, new_data)
        elif choice == 8:
            key = int(input("Enter the node to delete: "))
            dll.delete_node(key)
        elif choice == 9:
            dll.delete_first_node()
        elif choice == 10:
            dll.delete_last_node()
        elif choice == 11:
            print(f"Sum of all elements in the list: {dll.sum_of_elements()}")
        elif choice == 12:
            print("Maximum data in the linked list: ", dll.max_elements())
        elif choice == 13:
            print("Minimum data in the linked list: ", dll.min_elements())
        elif choice == 14:
            print("Number of elements in the linked list: ", dll.count())
        elif choice == 15:
            print("Done")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
