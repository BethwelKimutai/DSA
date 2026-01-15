"""
Arrays and Lists - Day 1 Implementation
========================================
This module contains comprehensive array operations and algorithms.
"""


class ArrayOperations:
    """Class containing various array operations and algorithms."""
    
    def __init__(self, arr=None):
        """Initialize with an array."""
        self.arr = arr if arr is not None else []
    
    def append(self, value):
        """Add an element to the end of the array."""
        self.arr.append(value)
        return self.arr
    
    def insert(self, index, value):
        """Insert an element at a specific index."""
        if 0 <= index <= len(self.arr):
            self.arr.insert(index, value)
            return self.arr
        raise IndexError("Index out of range")
    
    def delete(self, index):
        """Delete an element at a specific index."""
        if 0 <= index < len(self.arr):
            return self.arr.pop(index)
        raise IndexError("Index out of range")
    
    def find_min(self):
        """Find the minimum value in the array."""
        if not self.arr:
            return None
        min_val = self.arr[0]
        for i in self.arr:
            if i < min_val:
                min_val = i
        return min_val
    
    def find_max(self):
        """Find the maximum value in the array."""
        if not self.arr:
            return None
        max_val = self.arr[0]
        for i in self.arr:
            if i > max_val:
                max_val = i
        return max_val
    
    def linear_search(self, target):
        """Search for a target value using linear search."""
        for i, value in enumerate(self.arr):
            if value == target:
                return i
        return -1
    
    def reverse(self):
        """Reverse the array in-place."""
        left = 0
        right = len(self.arr) - 1
        while left < right:
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            left += 1
            right -= 1
        return self.arr
    
    def get_size(self):
        """Get the size of the array."""
        return len(self.arr)
    
    def is_empty(self):
        """Check if the array is empty."""
        return len(self.arr) == 0
    
    def display(self):
        """Display the array."""
        return self.arr


def find_second_largest(arr):
    """Find the second largest element in an array."""
    if len(arr) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else None


def remove_duplicates(arr):
    """Remove duplicates from an array while preserving order."""
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def rotate_array(arr, k):
    """Rotate array to the right by k positions."""
    if not arr or k == 0:
        return arr
    
    n = len(arr)
    k = k % n  # Handle k > n
    
    # Reverse entire array
    arr.reverse()
    # Reverse first k elements
    arr[:k] = reversed(arr[:k])
    # Reverse remaining elements
    arr[k:] = reversed(arr[k:])
    
    return arr


def two_sum(arr, target):
    """Find two numbers that add up to target. Returns indices."""
    num_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return None
