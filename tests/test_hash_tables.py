"""
Test file for Hash Tables - Day 6
==================================
Tests all hash table operations.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data_structures.hash_tables.hash_table import (
    HashTable,
    HashTableOpenAddressing,
    count_characters,
    find_duplicates,
    two_sum_hash
)


class TestHashTable:
    """Test cases for HashTable (chaining)."""
    
    def test_insert_get(self):
        """Test insert and get operations."""
        ht = HashTable()
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        assert ht.get("key1") == "value1"
        assert ht.get("key2") == "value2"
    
    def test_insert_update(self):
        """Test updating existing key."""
        ht = HashTable()
        ht.insert("key1", "value1")
        ht.insert("key1", "value2")
        assert ht.get("key1") == "value2"
    
    def test_delete(self):
        """Test delete operation."""
        ht = HashTable()
        ht.insert("key1", "value1")
        assert ht.delete("key1") == True
        assert ht.contains("key1") == False
        assert ht.delete("nonexistent") == False
    
    def test_contains(self):
        """Test contains method."""
        ht = HashTable()
        ht.insert("key1", "value1")
        assert ht.contains("key1") == True
        assert ht.contains("key2") == False
    
    def test_get_size(self):
        """Test size method."""
        ht = HashTable()
        assert ht.get_size() == 0
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        assert ht.get_size() == 2
    
    def test_integer_keys(self):
        """Test with integer keys."""
        ht = HashTable()
        ht.insert(1, "one")
        ht.insert(2, "two")
        assert ht.get(1) == "one"
        assert ht.get(2) == "two"


class TestHashTableOpenAddressing:
    """Test cases for HashTableOpenAddressing."""
    
    def test_insert_get(self):
        """Test insert and get operations."""
        ht = HashTableOpenAddressing()
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        assert ht.get("key1") == "value1"
        assert ht.get("key2") == "value2"
    
    def test_delete(self):
        """Test delete operation."""
        ht = HashTableOpenAddressing()
        ht.insert("key1", "value1")
        assert ht.delete("key1") == True
        assert ht.contains("key1") == False
    
    def test_contains(self):
        """Test contains method."""
        ht = HashTableOpenAddressing()
        ht.insert("key1", "value1")
        assert ht.contains("key1") == True
        assert ht.contains("key2") == False


class TestHashTableAlgorithms:
    """Test cases for hash table algorithms."""
    
    def test_count_characters(self):
        """Test character counting."""
        result = count_characters("hello")
        char_dict = dict(result)
        assert char_dict.get('l', 0) == 2
        assert char_dict.get('h', 0) == 1
    
    def test_find_duplicates(self):
        """Test finding duplicates."""
        assert find_duplicates([1, 2, 3, 2, 4, 3]) == [2, 3]
        assert find_duplicates([1, 2, 3]) == []
    
    def test_two_sum_hash(self):
        """Test two sum using hash table."""
        result = two_sum_hash([2, 7, 11, 15], 9)
        assert result == [0, 1] or result == [1, 0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
