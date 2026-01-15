"""
Binary Trees - Day 4 Implementation
====================================
This module contains binary tree and binary search tree implementations.
"""


class TreeNode:
    """Node class for binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Binary Tree implementation."""
    
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = TreeNode(root_value)
        else:
            self.root = None
    
    def insert(self, value):
        """Insert a value into the tree (level-order insertion)."""
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        from collections import deque
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            
            if node.left is None:
                node.left = TreeNode(value)
                return
            elif node.right is None:
                node.right = TreeNode(value)
                return
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def search(self, value):
        """Search for a value in the tree."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search."""
        if node is None:
            return False
        
        if node.value == value:
            return True
        
        return (self._search_recursive(node.left, value) or
                self._search_recursive(node.right, value))
    
    def height(self):
        """Calculate the height of the tree."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method for calculating height."""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)
    
    def count_nodes(self):
        """Count the total number of nodes."""
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node):
        """Helper method for counting nodes."""
        if node is None:
            return 0
        
        return (1 + self._count_nodes_recursive(node.left) +
                self._count_nodes_recursive(node.right))
    
    def is_empty(self):
        """Check if the tree is empty."""
        return self.root is None


class BinarySearchTree:
    """Binary Search Tree (BST) implementation."""
    
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = TreeNode(root_value)
        else:
            self.root = None
    
    def insert(self, value):
        """Insert a value into the BST."""
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method for recursive insertion."""
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        
        return node
    
    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search."""
        if node is None:
            return False
        
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method for recursive deletion."""
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has two children
                # Find in-order successor (smallest in right subtree)
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        """Find the minimum value node."""
        while node.left:
            node = node.left
        return node
    
    def find_min(self):
        """Find the minimum value in the BST."""
        if self.root is None:
            return None
        return self._find_min(self.root).value
    
    def find_max(self):
        """Find the maximum value in the BST."""
        if self.root is None:
            return None
        
        node = self.root
        while node.right:
            node = node.right
        return node.value
    
    def height(self):
        """Calculate the height of the BST."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method for calculating height."""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)
    
    def is_valid_bst(self):
        """Check if the tree is a valid BST."""
        return self._is_valid_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_recursive(self, node, min_val, max_val):
        """Helper method for BST validation."""
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._is_valid_recursive(node.left, min_val, node.value) and
                self._is_valid_recursive(node.right, node.value, max_val))
