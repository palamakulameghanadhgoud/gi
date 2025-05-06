class Node:
    """Linked list node for chaining"""
    def init(self, data):
        self.data = data
        self.next = None

class HashTable:
    """Hash Table using Chaining with Linked Lists"""
    def init(self, size):
        self.size = size
        self.chain = [None] * size  # Array of linked lists

    def hash_function(self, value):
        """Compute hash key"""
        return value % self.size

    def insert(self, value):
        """Insert value into hash table"""
        key = self.hash_function(value)
        new_node = Node(value)

        # If chain[key] is empty, insert at head
        if self.chain[key] is None:
            self.chain[key] = new_node
        else:
            # Traverse to the end and insert
            temp = self.chain[key]
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def search(self, value):
        """Search for a value in hash table"""
        key = self.hash_function(value)
        temp = self.chain[key]

        while temp:
            if temp.data == value:
                print(f"Element {value} found in chain[{key}]")
                return
            temp = temp.next

        print(f"Element {value} not found")

    def display(self):
        """Display the hash table"""
        for i in range(self.size):
            print(f"chain[{i}] -->", end=" ")
            temp = self.chain[i]
            while temp:
                print(f"{temp.data} -->", end=" ")
                temp = temp.next
            print("NULL")

# Main executio
hash_table = HashTable(10)

while True:
    print("\n1. Insert  2. Display  3. Search  4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        hash_table.insert(value)
    elif choice == 2:
        hash_table.display()
    elif choice == 3:
        value = int(input("Enter value to search: "))
        hash_table.search(value)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
