"""
Test file for Sorting Algorithms - Day 8
==========================================
Tests all sorting algorithms.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from algorithms.sorting.sorting_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    counting_sort
)


class TestSortingAlgorithms:
    """Test cases for sorting algorithms."""
    
    def test_bubble_sort(self):
        """Test bubble sort."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = bubble_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]
    
    def test_selection_sort(self):
        """Test selection sort."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = selection_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]
    
    def test_insertion_sort(self):
        """Test insertion sort."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = insertion_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]
    
    def test_merge_sort(self):
        """Test merge sort."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = merge_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]
    
    def test_quick_sort(self):
        """Test quick sort."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = quick_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]
    
    def test_heap_sort(self):
        """Test heap sort."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = heap_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]
    
    def test_counting_sort(self):
        """Test counting sort."""
        arr = [4, 2, 2, 8, 3, 3, 1]
        result = counting_sort(arr, 8)
        assert result == [1, 2, 2, 3, 3, 4, 8]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
