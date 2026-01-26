"""
Test file for Searching Algorithms - Day 9
===========================================
Tests all searching algorithms.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from algorithms.searching.searching_algorithms import (
    linear_search,
    binary_search,
    binary_search_recursive,
    interpolation_search,
    jump_search,
    exponential_search,
    find_first_occurrence,
    find_last_occurrence,
    count_occurrences
)


class TestSearchingAlgorithms:
    """Test cases for searching algorithms."""
    
    def test_linear_search(self):
        """Test linear search."""
        arr = [10, 20, 30, 40, 50]
        assert linear_search(arr, 30) == 2
        assert linear_search(arr, 60) == -1
    
    def test_binary_search(self):
        """Test binary search."""
        arr = [10, 20, 30, 40, 50]
        assert binary_search(arr, 30) == 2
        assert binary_search(arr, 60) == -1
    
    def test_binary_search_recursive(self):
        """Test recursive binary search."""
        arr = [10, 20, 30, 40, 50]
        assert binary_search_recursive(arr, 30) == 2
        assert binary_search_recursive(arr, 60) == -1
    
    def test_interpolation_search(self):
        """Test interpolation search."""
        arr = [10, 20, 30, 40, 50]
        assert interpolation_search(arr, 30) == 2
    
    def test_jump_search(self):
        """Test jump search."""
        arr = [10, 20, 30, 40, 50]
        assert jump_search(arr, 30) == 2
    
    def test_exponential_search(self):
        """Test exponential search."""
        arr = [10, 20, 30, 40, 50]
        assert exponential_search(arr, 30) == 2
    
    def test_find_first_occurrence(self):
        """Test finding first occurrence."""
        arr = [1, 2, 2, 2, 3, 4]
        assert find_first_occurrence(arr, 2) == 1
    
    def test_find_last_occurrence(self):
        """Test finding last occurrence."""
        arr = [1, 2, 2, 2, 3, 4]
        assert find_last_occurrence(arr, 2) == 3
    
    def test_count_occurrences(self):
        """Test counting occurrences."""
        arr = [1, 2, 2, 2, 3, 4]
        assert count_occurrences(arr, 2) == 3
        assert count_occurrences(arr, 5) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
