"""
Stacks - Day 3 Implementation
==============================
This module contains stack implementations using arrays and linked lists.
"""


class ArrayStack:
    """Stack implementation using array/list."""
    
    def __init__(self):
        self.items = []
    
    def push(self, value):
        """Add an element to the top of the stack."""
        self.items.append(value)
    
    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Get the size of the stack."""
        return len(self.items)
    
    def display(self):
        """Display all elements in the stack."""
        return self.items.copy()


class Node:
    """Node class for linked list stack."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    """Stack implementation using linked list."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        """Add an element to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.value
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.size == 0
    
    def get_size(self):
        """Get the size of the stack."""
        return self.size
    
    def display(self):
        """Display all elements in the stack."""
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values


def is_balanced_parentheses(s):
    """Check if parentheses are balanced using stack."""
    stack = ArrayStack()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()


def evaluate_postfix(expression):
    """Evaluate postfix expression using stack."""
    stack = ArrayStack()
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token not in operators:
            stack.push(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
    
    return stack.pop()


def reverse_string(s):
    """Reverse a string using stack."""
    stack = ArrayStack()
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str
