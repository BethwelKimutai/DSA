"""
Test file for Trees - Day 4 & 5
================================
Tests all tree operations and traversals.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.trees.binary_tree import (
    BinaryTree,
    BinarySearchTree,
    TreeNode
)
from data_structures.trees.tree_traversals import (
    inorder_traversal,
    preorder_traversal,
    postorder_traversal,
    level_order_traversal,
    level_order_traversal_levels,
    inorder_iterative,
    preorder_iterative,
    postorder_iterative,
    zigzag_traversal,
    find_max_depth,
    find_min_depth,
    count_leaves,
    sum_of_nodes
)


class TestBinaryTree:
    """Test cases for BinaryTree."""
    
    def test_insert(self):
        """Test inserting nodes."""
        tree = BinaryTree(1)
        tree.insert(2)
        tree.insert(3)
        assert tree.root.value == 1
        assert tree.root.left.value == 2
        assert tree.root.right.value == 3
    
    def test_search(self):
        """Test searching for values."""
        tree = BinaryTree(1)
        tree.insert(2)
        tree.insert(3)
        assert tree.search(2) == True
        assert tree.search(5) == False
    
    def test_height(self):
        """Test calculating height."""
        tree = BinaryTree(1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)
        assert tree.height() >= 1
    
    def test_count_nodes(self):
        """Test counting nodes."""
        tree = BinaryTree(1)
        tree.insert(2)
        tree.insert(3)
        assert tree.count_nodes() == 3


class TestBinarySearchTree:
    """Test cases for BinarySearchTree."""
    
    def test_insert(self):
        """Test inserting into BST."""
        bst = BinarySearchTree(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        assert bst.root.value == 5
        assert bst.root.left.value == 3
        assert bst.root.right.value == 7
    
    def test_search(self):
        """Test searching in BST."""
        bst = BinarySearchTree(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.search(3) == True
        assert bst.search(10) == False
    
    def test_find_min_max(self):
        """Test finding min and max."""
        bst = BinarySearchTree(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(9)
        assert bst.find_min() == 1
        assert bst.find_max() == 9
    
    def test_delete(self):
        """Test deleting from BST."""
        bst = BinarySearchTree(5)
        bst.insert(3)
        bst.insert(7)
        bst.delete(3)
        assert bst.search(3) == False
        assert bst.search(7) == True
    
    def test_is_valid_bst(self):
        """Test BST validation."""
        bst = BinarySearchTree(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.is_valid_bst() == True


class TestTreeTraversals:
    """Test cases for tree traversals."""
    
    @staticmethod
    def create_test_tree():
        """Create a test tree."""
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        return root
    
    def test_inorder_traversal(self):
        """Test in-order traversal."""
        root = self.create_test_tree()
        result = inorder_traversal(root)
        assert result == [4, 2, 5, 1, 3]
    
    def test_preorder_traversal(self):
        """Test pre-order traversal."""
        root = self.create_test_tree()
        result = preorder_traversal(root)
        assert result == [1, 2, 4, 5, 3]
    
    def test_postorder_traversal(self):
        """Test post-order traversal."""
        root = self.create_test_tree()
        result = postorder_traversal(root)
        assert result == [4, 5, 2, 3, 1]
    
    def test_level_order_traversal(self):
        """Test level-order traversal."""
        root = self.create_test_tree()
        result = level_order_traversal(root)
        assert result == [1, 2, 3, 4, 5]
    
    def test_inorder_iterative(self):
        """Test iterative in-order."""
        root = self.create_test_tree()
        result = inorder_iterative(root)
        assert result == [4, 2, 5, 1, 3]
    
    def test_preorder_iterative(self):
        """Test iterative pre-order."""
        root = self.create_test_tree()
        result = preorder_iterative(root)
        assert result == [1, 2, 4, 5, 3]
    
    def test_find_max_depth(self):
        """Test finding max depth."""
        root = self.create_test_tree()
        assert find_max_depth(root) == 3
    
    def test_count_leaves(self):
        """Test counting leaves."""
        root = self.create_test_tree()
        assert count_leaves(root) == 3
    
    def test_sum_of_nodes(self):
        """Test summing node values."""
        root = self.create_test_tree()
        assert sum_of_nodes(root) == 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
