#!/usr/bin/env python3
"""
Test utils.memoize function and understand its purpose
"""
memoized = __import__('utils').memoize


class MyClass:
    @memoize
    def a_method(self):
        print("a_method called")
        return 42

if __name__ == "__main__":
    my_object = MyClass()

    # Example 1
    print(my_object.a_method)
    # Output: a_method called
    #         42

    # Example 2
    print(my_object.a_method)
    # Output: 42

    # Example 3
    print(my_object.a_method)
    # Output: 42