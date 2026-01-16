"""
Tree Traversals - Day 5 Implementation
=======================================
This module contains various tree traversal algorithms.
"""

from collections import deque


class TreeNode:
    """Node class for binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    """In-order traversal: Left -> Root -> Right."""
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.value)
            inorder(node.right)
    
    inorder(root)
    return result



def preorder_traversal(root):
    """Pre-order traversal: Root -> Left -> Right."""
    result = []
    
    def preorder(node):
        if node:
            result.append(node.value)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result


def postorder_traversal(root):
    """Post-order traversal: Left -> Right -> Root."""
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.value)
    
    postorder(root)
    return result


def level_order_traversal(root):
    """Level-order (BFS) traversal."""
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


def level_order_traversal_levels(root):
    """Level-order traversal returning levels as separate lists."""
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


def inorder_iterative(root):
    """In-order traversal using iterative approach."""
    result = []
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.value)
        current = current.right
    
    return result


def preorder_iterative(root):
    """Pre-order traversal using iterative approach."""
    if root is None:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.value)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


def postorder_iterative(root):
    """Post-order traversal using iterative approach."""
    if root is None:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.value)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result[::-1]  # Reverse to get post-order


def zigzag_traversal(root):
    """Zigzag level-order traversal."""
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not left_to_right:
            level = level[::-1]
        
        result.extend(level)
        left_to_right = not left_to_right
    
    return result


def find_max_depth(root):
    """Find the maximum depth of a binary tree."""
    if root is None:
        return 0
    
    left_depth = find_max_depth(root.left)
    right_depth = find_max_depth(root.right)
    
    return 1 + max(left_depth, right_depth)


def find_min_depth(root):
    """Find the minimum depth of a binary tree."""
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    if root.left is None:
        return 1 + find_min_depth(root.right)
    
    if root.right is None:
        return 1 + find_min_depth(root.left)
    
    return 1 + min(find_min_depth(root.left), find_min_depth(root.right))


def count_leaves(root):
    """Count the number of leaf nodes."""
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return count_leaves(root.left) + count_leaves(root.right)


def sum_of_nodes(root):
    """Calculate the sum of all node values."""
    if root is None:
        return 0
    
    return root.value + sum_of_nodes(root.left) + sum_of_nodes(root.right)
