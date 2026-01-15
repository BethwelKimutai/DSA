# Day 4 - Thursday: Binary Trees and Binary Search Trees

**Date:** 15/01/2026 
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Trees - Binary Trees and BSTs

---

## Morning Session (8:00 AM - 1:00 PM)

### What I Learned

1. **Tree Basics**
   - Tree terminology:
     - Root, Node, Leaf, Edge
     - Parent, Child, Sibling
     - Depth, Height, Level
   - Tree properties:
     - Hierarchical structure
     - No cycles
     - N nodes = N-1 edges

2. **Binary Tree**
   - Each node has at most 2 children
   - Left child and right child
   - Can be complete, full, or perfect
   - Applications:
     - Expression trees
     - Decision trees
     - File systems

3. **Binary Search Tree (BST)**
   - Special binary tree with ordering property:
     - Left subtree < root
     - Right subtree > root
   - Enables efficient search: O(log n) average, O(n) worst
   - Operations:
     - Insert: O(log n) average
     - Search: O(log n) average
     - Delete: O(log n) average

### Code Written

- Created `data_structures/trees/binary_tree.py`
- Implemented `BinaryTree` class:
  - `insert(value)` - Level-order insertion
  - `search(value)` - Recursive search
  - `height()` - Calculate tree height
  - `count_nodes()` - Count total nodes
  - `is_empty()` - Check if empty

- Implemented `BinarySearchTree` class:
  - `insert(value)` - Maintain BST property
  - `search(value)` - Efficient search
  - `delete(value)` - Delete with 3 cases:
    1. No children: Simply remove
    2. One child: Replace with child
    3. Two children: Replace with in-order successor
  - `find_min()` - Find minimum value
  - `find_max()` - Find maximum value
  - `height()` - Calculate height
  - `is_valid_bst()` - Validate BST property

### Challenges Faced

- Understanding BST deletion with two children
- Finding in-order successor
- Maintaining BST property during operations
- Handling edge cases (empty tree, single node)

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Tree Properties**
   - Height vs Depth
   - Balanced vs Unbalanced trees
   - Complete binary tree
   - Full binary tree

2. **BST Operations Deep Dive**
   - Deletion algorithm:
     - Find node to delete
     - Handle three cases
     - Maintain BST property
   - Validation:
     - Check if tree maintains BST property
     - Use min/max bounds

### Code Written

- Completed BST implementation
- Added validation method
- Improved error handling

### Tests Performed

- Created test suite in `tests/test_trees.py`
- Tested:
  - Binary tree operations
  - BST operations
  - Edge cases
- All tests passing ✓

### Test Results

```
test_trees.py::TestBinaryTree::test_insert PASSED
test_trees.py::TestBinaryTree::test_search PASSED
test_trees.py::TestBinaryTree::test_height PASSED
test_trees.py::TestBinaryTree::test_count_nodes PASSED
test_trees.py::TestBinarySearchTree::test_insert PASSED
test_trees.py::TestBinarySearchTree::test_search PASSED
test_trees.py::TestBinarySearchTree::test_find_min_max PASSED
test_trees.py::TestBinarySearchTree::test_delete PASSED
test_trees.py::TestBinarySearchTree::test_is_valid_bst PASSED
```

---

## Summary

### Time Breakdown
- **Morning:** 5 hours (8 AM - 1 PM)
- **Lunch:** 1 hour (1 PM - 2 PM)
- **Afternoon:** 3 hours (2 PM - 5 PM)
- **Total:** 8 hours

### Files Created
1. `data_structures/trees/binary_tree.py` - Tree implementations

### Key Takeaways
- Trees are hierarchical data structures
- BST provides efficient search/insert/delete
- Deletion in BST requires careful handling
- Tree height affects operation complexity
- Balanced trees perform better

### Next Steps (Day 5)
- Study tree traversals
- Implement all traversal methods
- Learn iterative vs recursive approaches

---

## Notes
- BST deletion is complex but important
- Understanding tree properties helps with algorithms
- Ready to move to Day 5: Tree Traversals
