"""
    Fibonacci with Dynamic programming. We start with the most basic recursive solution,
    go to the top-down approach with memoization followed with the bottom up approach
    To time the implementation, use on ipython console: %%timeit followed by function
    For computing fibonacci of *35*
    Timing for fib_recursive_basic: 1 loop, best of 3: 2.18 s per loop
    Timing for fib_topdown: 100000 loops, best of 3: 12.8 µs per loop
    Timing for fib_bottomup: 100000 loops, best of 3: 4.19 µs per loop
"""
def fib_recursive_basic(n):
    if n == 1 or n == 2: return 1
    return fib_recursive_basic(n-1) + fib_recursive_basic(n-2)

"""
    DP Approach 1: Top-down approach with Memoization. Notice the calls to fib function stack up
"""
def fib_topdown(n):
    def fib(n, stored):
        if n in stored: return stored[n]
        if n == 1 or n == 2: return 1
        result = fib(n-1, stored) + fib(n-2, stored)
        stored[n] = result
        return result

    stored = {} # dictionary to store computed solutions
    return fib(n, stored)

"""
    DP Approach 2: Bottom-up approach with Memoization. Saves the function call stack size also
"""
def fib_bottomup(n):
    if n <= 0: return None
    if n == 1 or n == 2: return 1
    num_list = [1, 1] # init with the first 2 elements of fibonacci sequence
    curr = 3
    while curr <= n:
        num_list.append(num_list[-1] + num_list[-2])
        curr += 1
    return num_list[-1]

"""
    Given weights and values of n items, put these items in a knapsack of capacity W 
    to get the maximum total value in the knapsack. Given two integer arrays val[0..n-1] 
    and wt[0..n-1] which represent values and weights associated with n items respectively

    The max iterations with memoization is n*W: All items 1 to n are considered. For weight, 
    considering every possible weight between 0 and W (as the no. of different combination 
    of weights possible for each item i is W, W-1, W-2 ... 1)
    Hence, the algorithm complexity is O(N) as long as the the capacity W is small, if the 
    capacity W is itself O(N), the complexity is O(N^2)
"""
def call_knapsack(W, vals_list, weights_list):
    # List: rows are corresponding to weights, columns corresponding to items
    solutions_array = [[None for i in range(len(vals_list))] for j in range(W)]
    def knapsack_solution_topdown(W, vals_list, weights_list):
        if solutions_array[W][len(vals_list) - 1] is not None: return 
        if W == 0 or len(vals_list) == 0: # base case
            max_val, max_val_list = 0, []
        if len(vals_list) != len(weights_list): 
            raise Exception('Length of values list and weights list must be same')
        """
        NOTE: Need to start from end, because we don't need to pass an index tracker in function call
        If we decide to start from beginning, it is doable, but then we need to pass entire vals_list along 
        with the current index under consideration
        """
        item_idx = len(vals_list) - 1 
        if weight_list[item_idx] > W: # item weight is greater than capacity of sack
            knapsack_solution_topdown(W, vals_list[:-1], weights_list[:-1])
        else:
            val1, list1 = knapsack_solution_topdown(W, vals_list[:-1], weights_list[:-1])
            val2, list2 = knapsack_solution_topdown(W - weights_list[-1], vals_list[:-1], weights_list[:-1])
            max_val = max(val1, val2)
            if val1 > val2:
                max_val_list = 
        return max_val, max_val_list
