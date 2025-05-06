class Node:
    def init(self, data):
        self.data = data
        self.next = None

class Queue:
    
    def init(self):
        self.front = self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:  
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  
            self.rear = new_node      
        print(f"{data} enqueued to queue.")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        elif self.rear == self.front:
            t = self.front
            print("node being deleted", t.data)
            self.front = self.rear = None
            t = None
        else:
            t = self.front
            self.front = self.front.next
            print("node being deleted", t.data)
            t = None
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue contents:", end=" ")
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
def menu():
    queue = Queue()

    while True:
        print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert: "))
            queue.enqueue(data)
        elif choice == 2:
            deleted = queue.dequeue()
            if deleted is not None:
                print(f"Deleted data is {deleted}")
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Bye Bye!")
            break
        else:
            print("Invalid choice")

menu()
