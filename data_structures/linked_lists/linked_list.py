"""
Linked Lists - Day 2 Implementation
====================================
This module contains singly and doubly linked list implementations.
"""


class Node:
    """Node class for singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class DoublyNode:
    """Node class for doubly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SinglyLinkedList:
    """Singly Linked List implementation."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, value):
        """Add a node at the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, value):
        """Add a node at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at(self, index, value):
        """Insert a node at a specific index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(value)
            return
        
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, value):
        """Delete the first occurrence of a value."""
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def delete_at(self, index):
        """Delete node at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        value = current.next.value
        current.next = current.next.next
        self.size -= 1
        return value
    
    def search(self, value):
        """Search for a value in the list."""
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        """Get value at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def display(self):
        """Display the linked list."""
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
    
    def get_size(self):
        """Get the size of the list."""
        return self.size
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.size == 0


class DoublyLinkedList:
    """Doubly Linked List implementation."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, value):
        """Add a node at the end of the list."""
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
    
    def prepend(self, value):
        """Add a node at the beginning of the list."""
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, value):
        """Delete the first occurrence of a value."""
        current = self.head
        
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def display_forward(self):
        """Display the list from head to tail."""
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
    
    def display_backward(self):
        """Display the list from tail to head."""
        values = []
        current = self.tail
        while current:
            values.append(current.value)
            current = current.prev
        return values
    
    def get_size(self):
        """Get the size of the list."""
        return self.size
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.size == 0


def detect_cycle(head):
    """Detect if a linked list has a cycle using Floyd's algorithm."""
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False


def find_middle(head):
    """Find the middle node of a linked list."""
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.value if slow else None
