"""
Hash Tables - Day 6 Implementation
===================================
This module contains hash table implementations with collision handling.
"""


class HashTable:
    """Hash Table implementation using chaining for collision resolution."""
    
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key):
        """Hash function to determine bucket index."""
        if isinstance(key, int):
            return key % self.capacity
        elif isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.capacity
            return hash_value
        else:
            return hash(key) % self.capacity
    
    def insert(self, key, value):
        """Insert a key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor > 0.7
        if self.size > self.capacity * 0.7:
            self._resize()
    
    def get(self, key):
        """Get value for a key."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete a key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False
    
    def contains(self, key):
        """Check if key exists."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return True
        
        return False
    
    def _resize(self):
        """Resize the hash table when load factor is high."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        # Rehash all existing items
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)
    
    def get_size(self):
        """Get the number of key-value pairs."""
        return self.size
    
    def is_empty(self):
        """Check if hash table is empty."""
        return self.size == 0
    
    def display(self):
        """Display all key-value pairs."""
        result = []
        for bucket in self.buckets:
            for key, value in bucket:
                result.append((key, value))
        return result


class HashTableOpenAddressing:
    """Hash Table using open addressing (linear probing) for collision resolution."""
    
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.DELETED = object()  # Marker for deleted entries
    
    def _hash(self, key):
        """Hash function."""
        if isinstance(key, int):
            return key % self.capacity
        elif isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.capacity
            return hash_value
        else:
            return hash(key) % self.capacity
    
    def _probe(self, key):
        """Linear probing to find slot."""
        index = self._hash(key)
        start_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] != self.DELETED and self.keys[index] == key:
                return index
            index = (index + 1) % self.capacity
            if index == start_index:
                return -1  # Table is full
        
        return index
    
    def insert(self, key, value):
        """Insert a key-value pair."""
        if self.size >= self.capacity * 0.7:
            self._resize()
        
        index = self._probe(key)
        
        if index == -1:
            raise OverflowError("Hash table is full")
        
        if self.keys[index] is None or self.keys[index] == self.DELETED:
            self.size += 1
        
        self.keys[index] = key
        self.values[index] = value
    
    def get(self, key):
        """Get value for a key."""
        index = self._hash(key)
        start_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity
            if index == start_index:
                break
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete a key-value pair."""
        index = self._hash(key)
        start_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = self.DELETED
                self.values[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
            if index == start_index:
                break
        
        return False
    
    def contains(self, key):
        """Check if key exists."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def _resize(self):
        """Resize the hash table."""
        old_keys = self.keys
        old_values = self.values
        old_capacity = self.capacity
        
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        
        for i in range(old_capacity):
            if old_keys[i] is not None and old_keys[i] != self.DELETED:
                self.insert(old_keys[i], old_values[i])
    
    def get_size(self):
        """Get the number of key-value pairs."""
        return self.size
    
    def is_empty(self):
        """Check if hash table is empty."""
        return self.size == 0


def count_characters(s):
    """Count character frequencies using hash table."""
    char_count = HashTable()
    
    for char in s:
        if char_count.contains(char):
            char_count.insert(char, char_count.get(char) + 1)
        else:
            char_count.insert(char, 1)
    
    return char_count.display()


def find_duplicates(arr):
    """Find duplicate elements in an array."""
    seen = HashTable()
    duplicates = []
    
    for item in arr:
        if seen.contains(item):
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.insert(item, True)
    
    return duplicates


def two_sum_hash(arr, target):
    """Find two numbers that add up to target using hash table."""
    num_map = HashTable()
    
    for i, num in enumerate(arr):
        complement = target - num
        if num_map.contains(complement):
            return [num_map.get(complement), i]
        num_map.insert(num, i)
    
    return None
