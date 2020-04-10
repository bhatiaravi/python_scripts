from __future__ import print_function

"""
Simple O(N^2) selection sort
Find minimum element, assign it at end of the starting part of array at every step
Eg: selection_sort([12,3,14,5,16,71,19,21])
"""
def selection_sort(inp_list):
    if len(inp_list) == 0:
        return inp_list
    for idx in range(0, len(inp_list)):
        min_val_idx = idx # simply initialize
        for inner_idx in range(idx, len(inp_list)):
            if inp_list[inner_idx] < inp_list[min_val_idx]:
                min_val_idx = inner_idx
        inp_list[idx], inp_list[min_val_idx] = inp_list[min_val_idx], inp_list[idx]
    return inp_list

"""
Swapping adjacent elements repeatedly, if they are in wrong order. Do this 'n' times, where n is the length of array
Eg: bubble_sort([2,13,6,1,3,17,9,4])
"""
def bubble_sort(inp_list):
    if len(inp_list) == 0:
        return inp_list
    """
    Implementation 1: while loop, check if no. of swaps = 0 in a pass to ensure array sorted
    """
    not_sorted = True
    while not_sorted:
        num_swaps = 0
        for idx in range(0, len(inp_list) - 1): # here len of list - 1 needed because idx + 1 is being used for compare operation
            if inp_list[idx] > inp_list[idx + 1]:
                inp_list[idx], inp_list[idx + 1] = inp_list[idx + 1], inp_list[idx]
                num_swaps += 1
        if num_swaps == 0:
            not_sorted = False
    """
    Implementation 2: Slight improvement over above, using the fact that after kth pass, 
    only the starting n - k elements need to be considered, as last k have been sorted
    """
    for outer_idx in range(0, len(inp_list) - 1):
        for idx in range(0, len(inp_list) - outer_idx - 1):
            if inp_list[idx] > inp_list[idx + 1]:
                inp_list[idx], inp_list[idx + 1] = inp_list[idx + 1], inp_list[idx]
    return inp_list

def merge_lists(inp_list, left, mid, right): # merge 2 sorted lists into a single sorted list
    left_list = inp_list[left: mid+1] #  syntax: x[0:1] returns the 1st element
    right_list = inp_list[mid+1: right+1]
    #print("Left List to merge:", left_list)
    #print("Right List to merge:", right_list)
    l_idx, r_idx = 0, 0
    curr_idx = left
    while l_idx < len(left_list) and r_idx < len(right_list):
        if left_list[l_idx] < right_list[r_idx]: # if it is lower, take the element and assign to main array
            inp_list[curr_idx] = left_list[l_idx] # In-place substitution in input array
            l_idx += 1
        else:
            inp_list[curr_idx] = right_list[r_idx]
            r_idx += 1
        curr_idx += 1
    while l_idx < len(left_list): # For remaining elements of left array, if any
        inp_list[curr_idx] = left_list[l_idx]
        l_idx += 1
        curr_idx += 1
    while r_idx < len(right_list): # For remaining elements of right array, if any
        inp_list[curr_idx] = right_list[r_idx]
        r_idx += 1
        curr_idx += 1

    #print("Output after merge:", inp_list[left:right+1])
    return

""" Steps:
1. Divide input array in two halves recursively till the size of sub-list is 1
2. Merges the two sorted halves (assumes the 2 parts from previous step are sorted)

NOTE: Need to handle base case of 1 or 2 elements left in an array, sort them 
"""
def merge_sort_topdown(inp_list):
    def merge_sort(inp_list, left, right, num_calls):
        if left < right:
            mid = (left + right)/2
            num_calls.append(1)
            merge_sort(inp_list, left, mid, num_calls) # Could have used mid - 1 also, but problem of corner case when mid = 0
            merge_sort(inp_list, mid + 1, right, num_calls)
            merge_lists(inp_list, left, mid, right)

    if len(inp_list) <= 1:
        return inp_list
    left = 0
    right = len(inp_list) - 1
    num_calls = []
    merge_sort(inp_list, left, right, num_calls)
    print("List length:", len(inp_list))
    print("No. of Merge list calls", len(num_calls)/2)
    # NOTE: Each merge list call is considered O(N) complexity
    return inp_list

"""
    Merge sort with a Bottom-up approach. Why?
    As observed with the top-down approach, the function call stack of merge_sort function call
    keeps piling up. With the Bottom-up approach, we intend to minimize the call stack size.
    This is essentially an optimized use of memory for Merge sort
"""
def merge_sort_bottom_up(inp_list):
    

def quick_sort(inp_list):

"""
    Problem Description: Given 2 sorted arrays nums1 and nums2 (same or different size),
    find the median of the two sorted arrays
    Eg: find_median_sorted_lists([2,5,7,15], [1,4,9,10,13,16,18])
"""
def find_median_sorted_lists(nums1, nums2):
"""
    Approach 1: O(N) solution Idea.
    Use the same logic as merge_list step of merge_sort
"""
    def calc_median(arr):
        print arr
        mid = (len(arr) - 1)/2
        if len(arr) % 2 == 0: # even length
            return (arr[mid] + arr[mid + 1])/2.0
        else:
            return arr[mid]

    if len(nums1) == 0:
        return calc_median(nums2)
    if len(nums2) == 0:
        return calc_median(nums1)

    left_list = nums1 #  syntax: x[0:1] returns the 1st element
    right_list = nums2
    total_len = len(nums1) + len(nums2)
    mid = (total_len) / 2
    is_odd = True
    if total_len % 2 == 0:
        is_odd = False
    #print("Left List to merge:", left_list)
    #print("Right List to merge:", right_list)
    l_idx, r_idx, curr_idx = 0, 0, 0
    prev, curr = None, None

    while l_idx < len(left_list) and r_idx < len(right_list):
        prev = curr
        if left_list[l_idx] < right_list[r_idx]:
            curr = left_list[l_idx]
            l_idx += 1
        else:
            curr = right_list[r_idx]
            r_idx += 1
        if curr_idx == mid:
            if not is_odd:
                return calc_median([prev, curr])
            else:
                return curr
        curr_idx += 1

    while l_idx < len(left_list): # For remaining elements of left array, if any
        print "Remaining elements Left array"
        prev = curr
        curr = left_list[l_idx]
        if curr_idx == mid:
            if not is_odd:
                return calc_median([prev, curr])
            else:
                return curr
        l_idx += 1
        curr_idx += 1

    while r_idx < len(right_list): # For remaining elements of right array, if any
        prev = curr
        curr = right_list[r_idx]
        if curr_idx == mid:
            if not is_odd:
                return calc_median([prev, curr])
            else:
                return curr
        r_idx += 1
        curr_idx += 1

"""
    Approach 2: O(log(n)) solution Idea.
    Use the same logic as merge_list step of merge_sort
"""
