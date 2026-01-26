# Day 10 - Friday: Dynamic Programming

**Date:** 23/01/2025
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Dynamic Programming Basics

---

## Morning Session (8:00 AM - 1:00 PM)

### What I Learned

1. **Dynamic Programming Basics**
   - DP is optimization technique
   - Breaks problem into subproblems
   - Stores results to avoid recomputation
   - Two approaches:
     - Top-down (Memoization): Recursive with caching
     - Bottom-up (Tabulation): Iterative, build up

2. **DP Characteristics**
   - Optimal substructure: Optimal solution contains optimal sub-solutions
   - Overlapping subproblems: Same subproblems appear multiple times
   - Examples: Fibonacci, Factorial

3. **Fibonacci Example**
   - Naive recursive: O(2^n) time
   - DP: O(n) time, O(n) space
   - Optimized DP: O(n) time, O(1) space

### Code Written

- Created `algorithms/dynamic_programming/dp_algorithms.py`
- Implemented basic DP:
  - `fibonacci(n)` - DP with array
  - `fibonacci_optimized(n)` - DP with O(1) space

### Challenges Faced

- Understanding when to use DP
- Identifying optimal substructure
- Recognizing overlapping subproblems
- Choosing between memoization and tabulation

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Classic DP Problems**
   - **Longest Common Subsequence (LCS):**
     - Find longest common subsequence between two strings
     - Time: O(m*n), Space: O(m*n)
   - **Longest Increasing Subsequence (LIS):**
     - Find longest increasing subsequence
     - Time: O(n²), Space: O(n)
   - **Coin Change:**
     - Minimum coins to make amount
     - Time: O(amount * coins), Space: O(amount)
   - **0/1 Knapsack:**
     - Maximize value with weight constraint
     - Time: O(n * capacity), Space: O(n * capacity)
   - **Edit Distance (Levenshtein):**
     - Minimum operations to transform string
     - Time: O(m*n), Space: O(m*n)

2. **DP Patterns**
   - 1D DP: Fibonacci, Climbing stairs
   - 2D DP: LCS, Edit distance, Knapsack
   - Kadane's algorithm: Maximum subarray

### Code Written

- Implemented classic DP problems:
  - `longest_common_subsequence(s1, s2)` - LCS
  - `longest_increasing_subsequence(arr)` - LIS
  - `coin_change(coins, amount)` - Coin change
  - `knapsack(weights, values, capacity)` - 0/1 Knapsack
  - `edit_distance(s1, s2)` - Edit distance
  - `climb_stairs(n)` - Climbing stairs
  - `max_subarray_sum(arr)` - Kadane's algorithm
  - `unique_paths(m, n)` - Unique paths

### Tests Performed

- Created test suite in `tests/test_dynamic_programming.py`
- Tested all DP algorithms
- Verified with various test cases
- All tests passing ✓

### Test Results

```
test_dynamic_programming.py::TestDynamicProgramming::test_fibonacci PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_fibonacci_optimized PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_longest_common_subsequence PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_longest_increasing_subsequence PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_coin_change PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_knapsack PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_edit_distance PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_climb_stairs PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_max_subarray_sum PASSED
test_dynamic_programming.py::TestDynamicProgramming::test_unique_paths PASSED
```

---

## Summary

### Files Created
1. `algorithms/dynamic_programming/dp_algorithms.py` - DP algorithms

### Key Takeaways
- DP optimizes recursive solutions
- Identify optimal substructure and overlapping subproblems
- Memoization vs Tabulation trade-offs
- Space optimization is often possible
- DP solves many optimization problems
- Practice helps recognize DP patterns

### Week 2 Summary

**Completed Topics:**
1. ✅ Hash Tables
2. ✅ Graphs
3. ✅ Sorting Algorithms
4. ✅ Searching Algorithms
5. ✅ Dynamic Programming

**Total Files Created:** 10+
**Total Tests Written:** 50+
**All Tests Passing:** ✓

### 2-Week Journey Complete!

**Week 1:**
- Arrays and Lists
- Linked Lists
- Stacks and Queues
- Binary Trees and BSTs
- Tree Traversals

**Week 2:**
- Hash Tables
- Graphs
- Sorting Algorithms
- Searching Algorithms
- Dynamic Programming

**Total Implementation Files:** 20+
**Total Test Files:** 10
**Total Daily Logs:** 10
**All Code Tested and Documented:** ✓

---

## Notes
- 2-week journey complete!
- Strong foundation in data structures and algorithms
- All implementations are tested and documented
- Ready for advanced topics and problem-solving
