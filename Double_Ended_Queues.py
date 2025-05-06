class Deque:
    def __init__(self, size):
        self.size = size
        self.deque = [-1] * size
        self.front = -1
        self.rear = -1
        self.count = 0

    def insert_front(self, x):
        if (self.front == 0 and self.rear == self.size - 1) or(self.front == self.rear + 1):
            print("Overflow")
            return
      
        elif self.front == -1:
            self.front = self.rear = 0
            self.deque[self.front] = x
        

        elif self.front == 0:
            self.front = self.size - 1
            self.deque[self.front] = x
            
        else:
            self.front -= 1
            self.deque[self.front] = x
            
        self.count +=1
        
    def insert_rear(self, x):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            print("Overflow")
            return
        
        elif self.front == -1:
            self.front = self.rear = 0
            self.deque[self.rear] = x
            
        elif self.rear == self.size - 1:
            self.rear = 0
            self.deque[self.rear] = x
            
        else:
            self.rear += 1
            self.deque[self.rear] = x
        self.count +=1


    def get_front(self):
        if self.front == -1:
            print("Deque is empty")
        else:
            print("The value at front is:", self.deque[self.front])

    def get_rear(self):
        if self.rear == -1:
            print("Deque is empty")
        else:
            print("The value at rear is:", self.deque[self.rear])

    def delete_front(self):
        if self.front == -1:
            print("Deque is empty")
            return 
        elif self.front == self.rear:
            print("The deleted element is", self.deque[self.front])
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            print("The deleted element is", self.deque[self.front])
            self.front = 0
        else:
            print("The deleted element is", self.deque[self.front])
            self.front += 1
        self.count -=1
        
    def delete_rear(self):
        if self.rear == -1:
            print("Deque is empty")
            return
        elif self.front == self.rear:
            print("The deleted element is", self.deque[self.rear])
            self.front = self.rear = -1
        elif self.rear == 0:
            print("The deleted element is", self.deque[self.rear])
            self.rear = self.size - 1
        else:
            print("The deleted element is", self.deque[self.rear])
            self.rear -= 1
        self.count -=1

d = Deque(5)
d.insert_front(20)
d.insert_front(10)
d.insert_rear(30)
d.insert_rear(50)
d.insert_front(80)
d.get_front()
d.get_rear()
d.delete_front()
d.delete_rear()
