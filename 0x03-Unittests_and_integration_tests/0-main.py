#!/usr/bin/env python3
"""
Test utils.access_nested_map function and understand its purpose
"""
access_nested_map = __import__('utils').access_nested_map


nested_map1 = {"a": {"b": {"c": 1}}}
path1 = ["a", "b", "c"]
result1 = access_nested_map(nested_map1, path1)
print("Example 1:", result1)  # Output: 1

# Example 2
nested_map2 = {"x": {"y": {"z": "hello"}}}
path2 = ["x", "y", "z"]
result2 = access_nested_map(nested_map2, path2)
print("Example 2:", result2)  # Output: "hello"

# Example 3
nested_map3 = {"a": [1, 2, 3], "b": [4, 5, 6]}
path3 = ["b", 1]
result3 = access_nested_map(nested_map3, path3)
print("Example 3:", result3)  # Output: 5

# Example 4
nested_map4 = {"a": {"b": {"c": {"d": "example"}}}}
path4 = ["a", "b", "c", "d"]
result4 = access_nested_map(nested_map4, path4)
print("Example 4:", result4)  # Output: "example"
