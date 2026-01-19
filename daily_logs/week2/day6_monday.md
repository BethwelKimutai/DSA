# Day 6 - Monday: Hash Tables

**Date:** 19/01/2026
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Hash Tables and Hash Functions

---

## Morning Session (8:00 AM - 1:00 PM)

### What I Learned

1. **Hash Tables Basics**
   - Key-value pair storage
   - Average O(1) time for insert, search, delete
   - Hash function maps keys to array indices
   - Collision: When two keys hash to same index

2. **Hash Functions**
   - Good hash function properties:
     - Deterministic
     - Uniform distribution
     - Fast computation
   - Common techniques:
     - Division method: key % capacity
     - Multiplication method
     - String hashing: Polynomial rolling hash

3. **Collision Resolution - Chaining**
   - Each bucket is a list
   - Store multiple key-value pairs in same bucket
   - Simple to implement
   - Can handle any number of collisions
   - Space overhead for pointers

### Code Written

- Created `data_structures/hash_tables/hash_table.py`
- Implemented `HashTable` class (chaining):
  - `_hash(key)` - Hash function for int and string
  - `insert(key, value)` - Insert/update pair
  - `get(key)` - Retrieve value
  - `delete(key)` - Remove pair
  - `contains(key)` - Check existence
  - `_resize()` - Dynamic resizing
  - `get_size()` - Get number of pairs
  - `is_empty()` - Check if empty
  - `display()` - Show all pairs

### Challenges Faced

- Understanding hash function design
- Handling collisions properly
- Implementing dynamic resizing
- Choosing good load factor threshold

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Collision Resolution - Open Addressing**
   - Store directly in array
   - When collision occurs, probe for next available slot
   - Methods:
     - Linear probing: (hash + i) % capacity
     - Quadratic probing
     - Double hashing
   - Advantages: No extra memory for pointers
   - Disadvantages: Clustering, harder deletion

2. **Load Factor**
   - Ratio of elements to capacity
   - High load factor → more collisions
   - Resize when load factor > 0.7
   - Resize strategy: Double capacity, rehash all

3. **Hash Table Applications**
   - Character frequency counting
   - Finding duplicates
   - Two sum problem
   - Caching
   - Database indexing

### Code Written

- Implemented `HashTableOpenAddressing` class:
  - Linear probing for collision resolution
  - `_probe(key)` - Find slot using linear probing
  - `insert(key, value)` - Insert with probing
  - `get(key)` - Search with probing
  - `delete(key)` - Mark as deleted
  - `_resize()` - Resize and rehash

- Added hash table algorithms:
  - `count_characters(s)` - Character frequency
  - `find_duplicates(arr)` - Find duplicates
  - `two_sum_hash(arr, target)` - Two sum using hash

### Tests Performed

- Created test suite in `tests/test_hash_tables.py`
- Tested:
  - Chaining implementation
  - Open addressing implementation
  - Hash table algorithms
  - Edge cases
- All tests passing ✓

### Test Results

```
test_hash_tables.py::TestHashTable::test_insert_get PASSED
test_hash_tables.py::TestHashTable::test_insert_update PASSED
test_hash_tables.py::TestHashTable::test_delete PASSED
test_hash_tables.py::TestHashTable::test_contains PASSED
test_hash_tables.py::TestHashTable::test_get_size PASSED
test_hash_tables.py::TestHashTable::test_integer_keys PASSED
test_hash_tables.py::TestHashTableOpenAddressing::test_insert_get PASSED
test_hash_tables.py::TestHashTableOpenAddressing::test_delete PASSED
test_hash_tables.py::TestHashTableOpenAddressing::test_contains PASSED
test_hash_tables.py::TestHashTableAlgorithms::test_count_characters PASSED
test_hash_tables.py::TestHashTableAlgorithms::test_find_duplicates PASSED
test_hash_tables.py::TestHashTableAlgorithms::test_two_sum_hash PASSED
```

---

## Summary

### Time Breakdown
- **Morning:** 4 hours (8 AM - 1 PM)
- **Lunch:** 1 hour (1 PM - 2 PM)
- **Afternoon:** 4 hours (2 PM - 5 PM)
- **Total:** 8 hours

### Files Created
1. `data_structures/hash_tables/hash_table.py` - Hash table implementations

### Key Takeaways
- Hash tables provide O(1) average-case operations
- Collision handling is crucial
- Chaining vs Open addressing trade-offs
- Load factor affects performance
- Hash functions must distribute uniformly
- Resizing maintains efficiency

### Next Steps (Day 7)
- Study Graphs
- Understand graph representation
- Implement BFS and DFS
- Learn graph algorithms

---

## Notes
- Hash tables are fundamental for fast lookups
- Understanding collision resolution is important
- Ready to move to Day 7: Graphs
