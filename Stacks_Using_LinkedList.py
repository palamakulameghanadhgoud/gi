class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return None
        temp = self.head
        data = self.head.data
        self.head = self.head.next
        return data
    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return None
        return self.head.data
    def display(self):
        temp = self.head
        if self.head is None:
            print("Stack is empty")
            return None
        while temp is not None:
            print(temp.data)
            temp = temp.next
def main():
    size = int(input("Enter size of stack: "))
    stack = Stack()
    while True:
        print("\nStack Menu:")
        print("1. Push the stack")
        print("2. Pop the stack")
        print("3. Peek the stack")
        print("4. Display the stack")
        print("5. Exit")
        choice = int(input("Enter the choice operator: "))
        if choice == 1:
            data = int(input("Enter data to push: "))
            stack.push(data)
        elif choice == 2:
            popped_data = stack.pop()
            if popped_data is not None:
                print("Popped data: ", popped_data)
        elif choice == 3:
            top_data = stack.peek()
            if top_data is not None:
                print("Top data: ", top_data)
        elif choice == 4:
            print("Stack data: ")
            stack.display()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
        
