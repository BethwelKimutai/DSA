"""
Test file for Array Operations - Day 1
======================================
Tests all array operations and algorithms.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.arrays.array_operations import (
    ArrayOperations,
    find_second_largest,
    remove_duplicates,
    rotate_array,
    two_sum
)


class TestArrayOperations:
    """Test cases for ArrayOperations class."""
    
    def test_append(self):
        """Test appending elements."""
        arr_ops = ArrayOperations([1, 2, 3])
        result = arr_ops.append(4)
        assert result == [1, 2, 3, 4]
    
    def test_insert(self):
        """Test inserting at index."""
        arr_ops = ArrayOperations([1, 2, 3])
        result = arr_ops.insert(1, 5)
        assert result == [1, 5, 2, 3]
    
    def test_delete(self):
        """Test deleting at index."""
        arr_ops = ArrayOperations([1, 2, 3])
        deleted = arr_ops.delete(1)
        assert deleted == 2
        assert arr_ops.arr == [1, 3]
    
    def test_find_min(self):
        """Test finding minimum value."""
        arr_ops = ArrayOperations([5, 2, 8, 1, 9])
        assert arr_ops.find_min() == 1
    
    def test_find_max(self):
        """Test finding maximum value."""
        arr_ops = ArrayOperations([5, 2, 8, 1, 9])
        assert arr_ops.find_max() == 9
    
    def test_linear_search(self):
        """Test linear search."""
        arr_ops = ArrayOperations([5, 2, 8, 1, 9])
        assert arr_ops.linear_search(8) == 2
        assert arr_ops.linear_search(10) == -1
    
    def test_reverse(self):
        """Test reversing array."""
        arr_ops = ArrayOperations([1, 2, 3, 4])
        result = arr_ops.reverse()
        assert result == [4, 3, 2, 1]
    
    def test_get_size(self):
        """Test getting array size."""
        arr_ops = ArrayOperations([1, 2, 3])
        assert arr_ops.get_size() == 3
    
    def test_is_empty(self):
        """Test checking if array is empty."""
        arr_ops = ArrayOperations()
        assert arr_ops.is_empty() == True
        arr_ops.append(1)
        assert arr_ops.is_empty() == False


class TestArrayAlgorithms:
    """Test cases for array algorithms."""
    
    def test_find_second_largest(self):
        """Test finding second largest."""
        assert find_second_largest([1, 2, 3, 4, 5]) == 4
        assert find_second_largest([5, 5, 4, 3]) == 4
        assert find_second_largest([1]) == None
    
    def test_remove_duplicates(self):
        """Test removing duplicates."""
        assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
        assert remove_duplicates([1, 1, 1]) == [1]
    
    def test_rotate_array(self):
        """Test array rotation."""
        assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
        assert rotate_array([1, 2, 3], 0) == [1, 2, 3]
    
    def test_two_sum(self):
        """Test two sum problem."""
        result = two_sum([2, 7, 11, 15], 9)
        assert result == [0, 1]
        assert two_sum([3, 2, 4], 6) == [1, 2]
        assert two_sum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
