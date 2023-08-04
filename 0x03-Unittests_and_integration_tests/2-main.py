#!/usr/bin/env python3
"""
Test utils.get_json function and understand its purpose
"""
get_json = __import__('utils').get_json


# Example URL - Replace this with the actual URL of the JSON endpoint you want to access
example_url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    json_data = get_json(example_url)
    print("JSON data fetched successfully:")
    print(json_data)
except requests.exceptions.RequestException as e:
    print("Error occurred while fetching JSON data:", e)
