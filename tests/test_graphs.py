"""
Test file for Graphs - Day 7
=============================
Tests all graph operations.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.graphs.graph import Graph, WeightedGraph


class TestGraph:
    """Test cases for Graph."""
    
    def test_add_edge(self):
        """Test adding edges."""
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        assert len(g.get_neighbors(0)) == 2
    
    def test_bfs(self):
        """Test BFS traversal."""
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        result = g.bfs(0)
        assert 0 in result
        assert 1 in result
        assert 2 in result
        assert 3 in result
    
    def test_dfs(self):
        """Test DFS traversal."""
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        result = g.dfs(0)
        assert len(result) == 4
    
    def test_has_path(self):
        """Test path existence."""
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        assert g.has_path(0, 2) == True
        assert g.has_path(0, 5) == False
    
    def test_is_connected(self):
        """Test connectivity."""
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        assert g.is_connected() == True


class TestWeightedGraph:
    """Test cases for WeightedGraph."""
    
    def test_dijkstra(self):
        """Test Dijkstra's algorithm."""
        g = WeightedGraph()
        g.add_edge(0, 1, 4)
        g.add_edge(0, 2, 1)
        g.add_edge(2, 1, 2)
        distances = g.dijkstra(0)
        assert distances[1] == 3
        assert distances[2] == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
