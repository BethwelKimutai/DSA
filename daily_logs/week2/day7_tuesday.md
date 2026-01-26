# Day 7 - Tuesday: Graphs

**Date:** 20/1/2026
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Graphs - Representation and Algorithms

---

## Morning Session (8:00 AM - 1:00 PM)

### What I Learned

1. **Graph Basics**
   - Graph terminology:
     - Vertex/Node, Edge, Path, Cycle
     - Directed vs Undirected
     - Weighted vs Unweighted
     - Connected vs Disconnected
   - Graph representations:
     - Adjacency List: Space O(V+E), Good for sparse graphs
     - Adjacency Matrix: Space O(V²), Good for dense graphs

2. **Graph Traversals**
   - **BFS (Breadth-First Search):**
     - Uses queue
     - Finds shortest path in unweighted graphs
     - Time: O(V+E)
   - **DFS (Depth-First Search):**
     - Uses stack (recursive or iterative)
     - Explores as far as possible
     - Time: O(V+E)

### Code Written

- Created `data_structures/graphs/graph.py`
- Implemented `Graph` class:
  - `add_edge(u, v, weight)` - Add edge
  - `add_vertex(v)` - Add vertex
  - `get_vertices()` - Get all vertices
  - `get_edges()` - Get all edges
  - `get_neighbors(v)` - Get neighbors
  - `bfs(start)` - Breadth-first search
  - `dfs(start)` - Recursive DFS
  - `dfs_iterative(start)` - Iterative DFS
  - `has_path(start, end)` - Check path existence
  - `find_shortest_path_bfs(start, end)` - Shortest path
  - `is_connected()` - Check connectivity
  - `count_components()` - Count connected components

### Challenges Faced

- Understanding graph representations
- Implementing BFS and DFS correctly
- Handling disconnected graphs
- Finding shortest paths

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Weighted Graphs**
   - Edges have weights
   - Applications: Maps, networks, routing

2. **Shortest Path Algorithms**
   - **Dijkstra's Algorithm:**
     - Finds shortest path from source to all vertices
     - Works with non-negative weights
     - Uses priority queue
     - Time: O((V+E) log V) with binary heap

3. **Graph Applications**
   - Social networks
   - Web pages (links)
   - Maps and navigation
   - Dependency graphs
   - Network routing

### Code Written

- Implemented `WeightedGraph` class:
  - `add_edge(u, v, weight)` - Add weighted edge
  - `dijkstra(start)` - Dijkstra's algorithm

- Completed graph implementation

### Tests Performed

- Created test suite in `tests/test_graphs.py`
- Tested:
  - Graph operations
  - BFS and DFS
  - Path finding
  - Connectivity
  - Dijkstra's algorithm
- All tests passing ✓

### Test Results

```
test_graphs.py::TestGraph::test_add_edge PASSED
test_graphs.py::TestGraph::test_bfs PASSED
test_graphs.py::TestGraph::test_dfs PASSED
test_graphs.py::TestGraph::test_has_path PASSED
test_graphs.py::TestGraph::test_is_connected PASSED
test_graphs.py::TestWeightedGraph::test_dijkstra PASSED
```

---

### Files Created
1. `data_structures/graphs/graph.py` - Graph implementations

### Key Takeaways
- Graphs model relationships between entities
- BFS finds shortest paths in unweighted graphs
- DFS explores deeply before backtracking
- Adjacency list is efficient for sparse graphs
- Dijkstra's finds shortest paths in weighted graphs
- Graph algorithms are fundamental to many applications

### Next Steps (Day 8)
- Study Sorting Algorithms
- Understand time and space complexities
- Implement various sorting methods

---

## Notes
- Graphs are powerful for modeling real-world problems
- BFS and DFS are fundamental traversal methods
- Ready to move to Day 8: Sorting Algorithms
