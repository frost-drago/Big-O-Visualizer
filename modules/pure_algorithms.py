# Modules for pure time complexity algorithms

import time

def pure_n_factorial(a_list):
    """
    Pure O(n!)
    Returns time taken.
    """
    
    def generate_permutations(a_list):

        if len(a_list) == 0:
            return []
        if len(a_list) == 1:
            return [a_list]

        perms = []
        for i in range(len(a_list)):
            current_num = a_list[i]
            remaining_list = a_list[:i] + a_list[i+1:]
            for p in generate_permutations(remaining_list):
                perms.append([current_num] + p)
        return perms

    # RUN
    time_start = time.time()
    generate_permutations(a_list)
    time_end = time.time()
    time_diff = time_end - time_start
    return time_diff


def pure_2_to_the_power_of_n(a_list):
    """
    Pure O(2^n)
    Returns time taken.
    """

    def generate_subsets(nums):
        def backtrack(subset, i):
            if i == len(nums):
                subsets.append(subset[:])
                return

            # Include the current number
            subset.append(nums[i])
            backtrack(subset, i + 1)

            # Exclude the current number
            subset.pop()
            backtrack(subset, i + 1)

        subsets = []
        backtrack([], 0)
        return subsets
    
    # RUN
    time_start = time.time()
    generate_subsets(a_list)
    time_end = time.time()
    time_diff = time_end - time_start
    return time_diff


def pure_n_to_the_power_of_2(a_list):
    """
    Pure O(n^2)
    Returns time taken.
    """
    time_start = time.time()
    for i in a_list:
        for j in a_list:
            i + j
            pass
    time_end = time.time()
    time_diff = time_end - time_start
    return time_diff


def pure_n_times_log_n(a_list):
    """
    Pure O(n*log(n))
    Returns time taken.

    For this one I took the same algorithm as sorting_algorihms.merge_sort.
    """

    # Direction: left to right = small to big
    def merge_sort_recursion(a_list):
        """
        The recursion loop of the merge sort.
        """
        if len(a_list) <= 1:
            return a_list

        # Get midpoint and split the list into half
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        left_half = merge_sort_recursion(left_half)
        right_half = merge_sort_recursion(right_half)

        return merge(left_half, right_half)

    def merge(left_list, right_list):
        """
        Merges two sorted lists into a single sorted list.
        """
        merged = []
        left_index = 0
        right_index = 0

        # Build the left and right list
        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                merged.append(left_list[left_index])
                left_index += 1
            else:
                merged.append(right_list[right_index])
                right_index += 1

        # Put the two lists together
        merged.extend(left_list[left_index:])
        merged.extend(right_list[right_index:])

        return merged
    
    # RUN
    time_start = time.time()
    merge_sort_recursion(a_list)
    time_end = time.time()
    time_diff = time_end - time_start
    return time_diff


def pure_n(a_list):
    """
    Pure O(n)
    Returns time taken.
    """
    time_start = time.time()
    for i in a_list:
        i
        pass
    time_end = time.time()
    time_diff = time_end - time_start
    return time_diff


def pure_log_n(a_list):
    """
    Pure O(log(n))
    Returns time taken.
    """
    def iterative_logarithm(a_list):
        n = len(a_list)
        count = 0
        while n > 1:
            n //= 2
            count += 1
        return count
    
    # RUN
    time_start = time.time()
    iterative_logarithm(a_list)
    time_end = time.time()
    time_diff = time_end - time_start
    return time_diff


def pure_1(a_list):
    """
    Pure O(1)
    Returns time taken.
    """
    time_start = time.time()
    pass  # a_list is not used, just loaded into the function
    time_end = time.time()
    time_diff = time_end - time_start
    return time_diff