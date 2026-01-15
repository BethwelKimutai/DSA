"""
Test file for Linked Lists - Day 2
==================================
Tests all linked list operations.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.linked_lists.linked_list import (
    SinglyLinkedList,
    DoublyLinkedList,
    Node,
    detect_cycle,
    find_middle
)


class TestSinglyLinkedList:
    """Test cases for SinglyLinkedList."""
    
    def test_append(self):
        """Test appending nodes."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.display() == [1, 2, 3]
        assert ll.get_size() == 3
    
    def test_prepend(self):
        """Test prepending nodes."""
        ll = SinglyLinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)
        assert ll.display() == [3, 2, 1]
    
    def test_insert_at(self):
        """Test inserting at index."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(3)
        ll.insert_at(1, 2)
        assert ll.display() == [1, 2, 3]
    
    def test_delete(self):
        """Test deleting by value."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete(2) == True
        assert ll.display() == [1, 3]
        assert ll.delete(5) == False
    
    def test_delete_at(self):
        """Test deleting at index."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete_at(1) == 2
        assert ll.display() == [1, 3]
    
    def test_search(self):
        """Test searching for value."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.search(2) == 1
        assert ll.search(5) == -1
    
    def test_get(self):
        """Test getting value at index."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.get(1) == 2
    
    def test_reverse(self):
        """Test reversing the list."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()
        assert ll.display() == [3, 2, 1]
    
    def test_is_empty(self):
        """Test checking if empty."""
        ll = SinglyLinkedList()
        assert ll.is_empty() == True
        ll.append(1)
        assert ll.is_empty() == False


class TestDoublyLinkedList:
    """Test cases for DoublyLinkedList."""
    
    def test_append(self):
        """Test appending nodes."""
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        assert dll.display_forward() == [1, 2, 3]
        assert dll.display_backward() == [3, 2, 1]
    
    def test_prepend(self):
        """Test prepending nodes."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.prepend(2)
        dll.prepend(3)
        assert dll.display_forward() == [3, 2, 1]
    
    def test_delete(self):
        """Test deleting by value."""
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        assert dll.delete(2) == True
        assert dll.display_forward() == [1, 3]
        assert dll.delete(5) == False


class TestLinkedListAlgorithms:
    """Test cases for linked list algorithms."""
    
    def test_detect_cycle(self):
        """Test cycle detection."""
        # Create a list without cycle
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next = node2
        node2.next = node3
        assert detect_cycle(node1) == False
        
        # Create a list with cycle
        node1.next = node2
        node2.next = node3
        node3.next = node2  # Cycle
        assert detect_cycle(node1) == True
    
    def test_find_middle(self):
        """Test finding middle node."""
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert find_middle(ll.head) == 2
        
        ll.append(4)
        assert find_middle(ll.head) == 2  # Lower middle for even length


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
