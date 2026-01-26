"""
Graphs - Day 7 Implementation
==============================
This module contains graph implementations and algorithms.
"""

from collections import deque, defaultdict


class Graph:
    """Graph implementation using adjacency list."""
    
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        """Add an edge between vertices u and v."""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def add_vertex(self, v):
        """Add a vertex to the graph."""
        if v not in self.graph:
            self.graph[v] = []
    
    def get_vertices(self):
        """Get all vertices."""
        return list(self.graph.keys())
    
    def get_edges(self):
        """Get all edges."""
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                if self.directed or u < v:  # Avoid duplicates in undirected
                    edges.append((u, v, weight))
        return edges
    
    def get_neighbors(self, v):
        """Get neighbors of a vertex."""
        return self.graph.get(v, [])
    
    def bfs(self, start):
        """Breadth-First Search starting from 'start'."""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Depth-First Search starting from 'start'."""
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def dfs_iterative(self, start):
        """Iterative DFS."""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                for neighbor, _ in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def has_path(self, start, end):
        """Check if there's a path from start to end."""
        visited = set()
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            
            if vertex == end:
                return True
            
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, _ in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return False
    
    def find_shortest_path_bfs(self, start, end):
        """Find shortest path using BFS (unweighted graph)."""
        if start == end:
            return [start]
        
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        
        while queue:
            vertex, path = queue.popleft()
            
            for neighbor, _ in self.get_neighbors(vertex):
                if neighbor == end:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # No path found
    
    def is_connected(self):
        """Check if graph is connected (for undirected graphs)."""
        if not self.graph:
            return True
        
        vertices = self.get_vertices()
        if not vertices:
            return True
        
        start = vertices[0]
        visited = self.bfs(start)
        return len(visited) == len(vertices)
    
    def count_components(self):
        """Count connected components."""
        visited = set()
        components = 0
        
        for vertex in self.get_vertices():
            if vertex not in visited:
                components += 1
                # BFS to mark all connected vertices
                queue = deque([vertex])
                visited.add(vertex)
                
                while queue:
                    v = queue.popleft()
                    for neighbor, _ in self.get_neighbors(v):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return components


class WeightedGraph:
    """Weighted graph implementation."""
    
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight):
        """Add a weighted edge."""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def dijkstra(self, start):
        """Dijkstra's algorithm for shortest paths."""
        import heapq
        
        distances = {v: float('inf') for v in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if u in visited:
                continue
            
            visited.add(u)
            
            for v, weight in self.graph[u]:
                if v not in visited:
                    new_dist = current_dist + weight
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
        
        return distances
