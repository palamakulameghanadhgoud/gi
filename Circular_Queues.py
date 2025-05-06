
class CircularQueue:
    def init(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("\nCircular Queue is full")
            return
        
        if self.rear == -1:  
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        
        self.queue[self.rear] = data
    
    def dequeue(self):
        if self.front == -1:
            print("\nCQ is empty")
            return None
        
        data = self.queue[self.front]
        
        if self.front == self.rear:  
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return data
    
    def display(self):
        if self.front == -1:
            print("\nQueue is empty")
            return
        
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
def menu():
    size = int(input("Enter queue size"))
    cq = CircularQueue(size)
    
    while True:
        print("\nEnter your choice:")
        print("1. Insert\n2. Delete\n3. Display\n4. Exit")
        choice = int(input())
        
        if choice == 1:
            data = int(input("Enter the element you want to insert: "))
            cq.enqueue(data)
        elif choice == 2:
            removed = cq.dequeue()
            if removed is not None:
                print(f"\n{removed} is deleted")
        elif choice == 3:
            cq.display()
        elif choice == 4:
            break
        else:
            print("\nPlease enter a valid choice")
            
            
            
            
            
menu()
