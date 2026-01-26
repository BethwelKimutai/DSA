"""
Test file for Dynamic Programming - Day 10
==========================================
Tests all DP algorithms.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from algorithms.dynamic_programming.dp_algorithms import (
    fibonacci,
    fibonacci_optimized,
    longest_common_subsequence,
    longest_increasing_subsequence,
    coin_change,
    knapsack,
    edit_distance,
    climb_stairs,
    max_subarray_sum,
    unique_paths
)


class TestDynamicProgramming:
    """Test cases for DP algorithms."""
    
    def test_fibonacci(self):
        """Test fibonacci."""
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55
    
    def test_fibonacci_optimized(self):
        """Test optimized fibonacci."""
        assert fibonacci_optimized(5) == 5
        assert fibonacci_optimized(10) == 55
    
    def test_longest_common_subsequence(self):
        """Test LCS."""
        assert longest_common_subsequence("ABCDGH", "AEDFHR") == 3
        assert longest_common_subsequence("AGGTAB", "GXTXAYB") == 4
    
    def test_longest_increasing_subsequence(self):
        """Test LIS."""
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    def test_coin_change(self):
        """Test coin change."""
        assert coin_change([1, 3, 4], 6) == 2
        assert coin_change([2], 3) == -1
    
    def test_knapsack(self):
        """Test knapsack."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        assert knapsack(weights, values, capacity) == 9
    
    def test_edit_distance(self):
        """Test edit distance."""
        assert edit_distance("kitten", "sitting") == 3
        assert edit_distance("", "") == 0
    
    def test_climb_stairs(self):
        """Test climbing stairs."""
        assert climb_stairs(3) == 3
        assert climb_stairs(5) == 8
    
    def test_max_subarray_sum(self):
        """Test maximum subarray sum."""
        assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    
    def test_unique_paths(self):
        """Test unique paths."""
        assert unique_paths(3, 7) == 28


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
