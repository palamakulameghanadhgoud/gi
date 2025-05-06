# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 10:54:03 2025

@author: sairam
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        hkey = self.hash_function(key)
        for i in range(self.size):
            index = (hkey + i) % self.size
            if self.table[index] == -1:  # Empty slot found
                self.table[index] = key
                print(f"Inserted {key} at index {index}")
                return
        print("Element cannot be inserted (Table Full)")

    def search(self, key):
        hkey = self.hash_function(key)
        for i in range(self.size):
            index = (hkey + i) % self.size
            if self.table[index] == key:
                print(f"Value found at index {index}")
                return index
            if self.table[index] == -1:
                break  # Stop searching if an empty slot is encountered
        print("Value not found")
        return None

    def display(self):
        print("\nElements in the hash table:")
        for i, value in enumerate(self.table):
            print(f"Index {i}: {value}")

# Example usage
#if __name__ == "__main__":
hash_table = HashTable(10)
while True:
    print("\nPress 1. Insert  2. Display  3. Search  4. Exit")
    opt = int(input())
    if opt == 1:
        key = int(input("Enter a value to insert into the hash table: "))
        hash_table.insert(key)
    elif opt == 2:
        hash_table.display()
    elif opt == 3:
        key = int(input("Enter search element: "))
        hash_table.search(key)
    elif opt == 4:
        break
    else:
        print("Invalid option, try again.")
