"""
Binary search basic: Recursive, Iterative
"""

def binary_search_recursive(input_list, num_find):
    """
    Input: Provide a list, num_find (number to be searched for)
    Output: returns True if found, False if not found
    NOTE: Input List must be sorted
    """
    def search(input_list, num_find, left, right):
        if left > right:
            return False
        mid = (left + right)/2
        if num_find == input_list[mid]:
            return True
        elif num_find < input_list[mid]:
            right = mid - 1
            return search(input_list, num_find, left, right)
        elif num_find > input_list[mid]:
            left = mid + 1
            return search(input_list, num_find, left, right)
    
    left = 0
    right = len(input_list) - 1
    if len(input_list) == 0: # Base case, empty input list
        return False
    return search(input_list, num_find, left, right)

def binary_search_iterative(input_list, num_find):
    """
    Same as recursive binary search, but iterative way
    """
    if len(input_list) == 0: # Base case, empty input list
        return False
    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = (left + right)/2
        if num_find == input_list[mid]:
            return True
        elif num_find < input_list[mid]:
            right = mid - 1
        elif num_find > input_list[mid]:
            left = mid + 1
    return False # not found after loop completion
