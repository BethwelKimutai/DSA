"""
Queues - Day 3 Implementation
=============================
This module contains queue implementations using arrays and linked lists.
"""


class ArrayQueue:
    """Queue implementation using array/list."""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, value):
        """Add an element to the rear of the queue."""
        self.items.append(value)
    
    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def rear(self):
        """Return the rear element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Get the size of the queue."""
        return len(self.items)
    
    def display(self):
        """Display all elements in the queue."""
        return self.items.copy()


class Node:
    """Node class for linked list queue."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    """Queue implementation using linked list."""
    
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.size = 0
    
    def enqueue(self, value):
        """Add an element to the rear of the queue."""
        new_node = Node(value)
        
        if self.is_empty():
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        
        self.size += 1
    
    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        value = self.front_node.value
        self.front_node = self.front_node.next
        
        if self.front_node is None:
            self.rear_node = None
        
        self.size -= 1
        return value
    
    def front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front_node.value
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0
    
    def get_size(self):
        """Get the size of the queue."""
        return self.size
    
    def display(self):
        """Display all elements in the queue."""
        values = []
        current = self.front_node
        while current:
            values.append(current.value)
            current = current.next
        return values


class CircularQueue:
    """Circular Queue implementation using array."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, value):
        """Add an element to the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = value
        self.size += 1
    
    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def front_element(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.front]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity
    
    def get_size(self):
        """Get the size of the queue."""
        return self.size


class Deque:
    """Double-ended queue (Deque) implementation."""
    
    def __init__(self):
        self.items = []
    
    def add_front(self, value):
        """Add an element to the front."""
        self.items.insert(0, value)
    
    def add_rear(self, value):
        """Add an element to the rear."""
        self.items.append(value)
    
    def remove_front(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)
    
    def remove_rear(self):
        """Remove and return the rear element."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()
    
    def peek_front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[0]
    
    def peek_rear(self):
        """Return the rear element without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Get the size of the deque."""
        return len(self.items)
    
    def display(self):
        """Display all elements in the deque."""
        return self.items.copy()
