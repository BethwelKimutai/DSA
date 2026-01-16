# Day 5 - Friday: Tree Traversals and Operations

**Date:** 16/01/2026
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Tree Traversals and Advanced Operations

---

## Morning Session (8:00 AM - 12:00 PM)

### What I Learned

1. **Tree Traversals**
   - **In-order (Left-Root-Right):**
     - For BST: Returns sorted order
     - Time: O(n), Space: O(h)
   - **Pre-order (Root-Left-Right):**
     - Used for copying trees
     - Time: O(n), Space: O(h)
   - **Post-order (Left-Right-Root):**
     - Used for deleting trees
     - Time: O(n), Space: O(h)
   - **Level-order (BFS):**
     - Visit level by level
     - Uses queue
     - Time: O(n), Space: O(w) where w is max width

2. **Recursive vs Iterative**
   - Recursive: Simple, uses call stack
   - Iterative: More control, uses explicit stack/queue
   - Both have O(n) time complexity

### Code Written

- Created `data_structures/trees/tree_traversals.py`
- Implemented recursive traversals:
  - `inorder_traversal(root)` - L-Root-R
  - `preorder_traversal(root)` - Root-L-R
  - `postorder_traversal(root)` - L-R-Root
  - `level_order_traversal(root)` - BFS

- Implemented iterative traversals:
  - `inorder_iterative(root)` - Using stack
  - `preorder_iterative(root)` - Using stack
  - `postorder_iterative(root)` - Using stack

- Added level-order variants:
  - `level_order_traversal_levels(root)` - Returns levels as lists
  - `zigzag_traversal(root)` - Alternate left-right

### Challenges Faced

- Understanding stack usage in iterative traversals
- Implementing post-order iteratively
- Handling null nodes correctly
- Managing stack/queue state

---

## Afternoon Session (1:00 PM - 5:00 PM)

### What I Learned

1. **Tree Operations**
   - Finding depth (max and min)
   - Counting leaves
   - Summing node values
   - These operations use tree traversal

2. **Advanced Concepts**
   - Zigzag traversal: Alternate direction per level
   - Level-by-level processing
   - Tree property calculations

### Code Written

- Added tree operation functions:
  - `find_max_depth(root)` - Maximum depth
  - `find_min_depth(root)` - Minimum depth
  - `count_leaves(root)` - Count leaf nodes
  - `sum_of_nodes(root)` - Sum all values

- Completed all traversal implementations

### Tests Performed

- Extended test suite in `tests/test_trees.py`
- Tested:
  - All traversal methods (recursive and iterative)
  - Tree operations
  - Edge cases
- All tests passing ✓

### Test Results

```
test_trees.py::TestTreeTraversals::test_inorder_traversal PASSED
test_trees.py::TestTreeTraversals::test_preorder_traversal PASSED
test_trees.py::TestTreeTraversals::test_postorder_traversal PASSED
test_trees.py::TestTreeTraversals::test_level_order_traversal PASSED
test_trees.py::TestTreeTraversals::test_inorder_iterative PASSED
test_trees.py::TestTreeTraversals::test_preorder_iterative PASSED
test_trees.py::TestTreeTraversals::test_find_max_depth PASSED
test_trees.py::TestTreeTraversals::test_count_leaves PASSED
test_trees.py::TestTreeTraversals::test_sum_of_nodes PASSED
```

---

## Summary

### Time Breakdown
- **Morning:** 5 hours (8 AM - 1 PM)
- **Lunch:** 1 hour (1 PM - 2 PM)
- **Afternoon:** 3 hours (2 PM - 5 PM)
- **Total:** 8 hours

### Files Created
1. `data_structures/trees/tree_traversals.py` - Traversal implementations

### Key Takeaways
- Four main traversal types, each with specific use cases
- Recursive is simpler, iterative gives more control
- Level-order uses BFS (queue)
- In-order on BST gives sorted order
- Tree operations build on traversal concepts

### Week 1 Summary

**Completed Topics:**
1. ✅ Arrays and Lists
2. ✅ Linked Lists (Singly and Doubly)
3. ✅ Stacks and Queues
4. ✅ Binary Trees and BSTs
5. ✅ Tree Traversals

**Total Files Created:** 10+
**Total Tests Written:** 50+
**All Tests Passing:** ✓

### Next Steps (Week 2, Day 6)
- Study Hash Tables
- Understand hash functions and collision handling
- Implement hash table with chaining and open addressing

---

## Notes
- Week 1 complete! Strong foundation in basic data structures
- Ready for Week 2: Advanced structures and algorithms
- All code is well-documented and tested
