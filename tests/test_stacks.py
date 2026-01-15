"""
Test file for Stacks - Day 3
============================
Tests all stack operations.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.stacks.stack import (
    ArrayStack,
    LinkedStack,
    is_balanced_parentheses,
    evaluate_postfix,
    reverse_string
)


class TestArrayStack:
    """Test cases for ArrayStack."""
    
    def test_push_pop(self):
        """Test push and pop operations."""
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
    
    def test_peek(self):
        """Test peek operation."""
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.size() == 2
    
    def test_is_empty(self):
        """Test empty check."""
        stack = ArrayStack()
        assert stack.is_empty() == True
        stack.push(1)
        assert stack.is_empty() == False
    
    def test_size(self):
        """Test size method."""
        stack = ArrayStack()
        assert stack.size() == 0
        stack.push(1)
        stack.push(2)
        assert stack.size() == 2


class TestLinkedStack:
    """Test cases for LinkedStack."""
    
    def test_push_pop(self):
        """Test push and pop operations."""
        stack = LinkedStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
    
    def test_peek(self):
        """Test peek operation."""
        stack = LinkedStack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
    
    def test_is_empty(self):
        """Test empty check."""
        stack = LinkedStack()
        assert stack.is_empty() == True
        stack.push(1)
        assert stack.is_empty() == False


class TestStackAlgorithms:
    """Test cases for stack algorithms."""
    
    def test_balanced_parentheses(self):
        """Test parentheses balancing."""
        assert is_balanced_parentheses("()") == True
        assert is_balanced_parentheses("()[]{}") == True
        assert is_balanced_parentheses("([{}])") == True
        assert is_balanced_parentheses("([)]") == False
        assert is_balanced_parentheses("(((") == False
    
    def test_evaluate_postfix(self):
        """Test postfix evaluation."""
        assert evaluate_postfix("3 4 +") == 7
        assert evaluate_postfix("5 2 + 8 *") == 56
        assert evaluate_postfix("10 2 /") == 5
    
    def test_reverse_string(self):
        """Test string reversal."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("abc") == "cba"
        assert reverse_string("") == ""


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
