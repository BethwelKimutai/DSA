"""
Test file for Queues - Day 3
============================
Tests all queue operations.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.queues.queue import (
    ArrayQueue,
    LinkedQueue,
    CircularQueue,
    Deque
)


class TestArrayQueue:
    """Test cases for ArrayQueue."""
    
    def test_enqueue_dequeue(self):
        """Test enqueue and dequeue operations."""
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
    
    def test_front_rear(self):
        """Test front and rear methods."""
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.front() == 1
        assert queue.rear() == 2
    
    def test_is_empty(self):
        """Test empty check."""
        queue = ArrayQueue()
        assert queue.is_empty() == True
        queue.enqueue(1)
        assert queue.is_empty() == False


class TestLinkedQueue:
    """Test cases for LinkedQueue."""
    
    def test_enqueue_dequeue(self):
        """Test enqueue and dequeue operations."""
        queue = LinkedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
    
    def test_front(self):
        """Test front method."""
        queue = LinkedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.front() == 1


class TestCircularQueue:
    """Test cases for CircularQueue."""
    
    def test_enqueue_dequeue(self):
        """Test enqueue and dequeue operations."""
        queue = CircularQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        queue.enqueue(4)
        assert queue.dequeue() == 3
    
    def test_is_full(self):
        """Test full check."""
        queue = CircularQueue(2)
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.is_full() == True


class TestDeque:
    """Test cases for Deque."""
    
    def test_add_remove_front(self):
        """Test front operations."""
        deque = Deque()
        deque.add_front(1)
        deque.add_front(2)
        assert deque.remove_front() == 2
        assert deque.remove_front() == 1
    
    def test_add_remove_rear(self):
        """Test rear operations."""
        deque = Deque()
        deque.add_rear(1)
        deque.add_rear(2)
        assert deque.remove_rear() == 2
        assert deque.remove_rear() == 1
    
    def test_peek(self):
        """Test peek methods."""
        deque = Deque()
        deque.add_front(1)
        deque.add_rear(2)
        assert deque.peek_front() == 1
        assert deque.peek_rear() == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
