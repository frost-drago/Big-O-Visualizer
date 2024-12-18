# This module is dedicated to sorting algorithms.
# For all functions in here, generates (returns) a sorted list without modifying the original list.
# - a_list = (a list of ints) to be sorted.

def bubble_sort(a_list):
    """
    Theoretical results (real life differ):
    Average case:   O(n^2)
    Best case:      O(n)
    Worst case:     O(n^2)
    """
    copied_list = a_list[:]
    length = len(a_list)

    # Direction: left to right = small to big
    # Pushes biggest number to rightmost then it's counted as sorted
    for i in range(length - 1):
        for j in range(0, (length - i - 1)):
            # Swap if left > right
            if copied_list[j] > copied_list[j + 1]:
                copied_list[j], copied_list[j + 1] = copied_list[j + 1], copied_list[j]
    
    return copied_list


def selection_sort(a_list):
    """
    Theoretical results (real life differ):
    Average case:   O(n^2)
    Best case:      O(n^2)
    Worst case:     O(n^2)
    """

    copied_list = a_list[:]
    length = len(a_list)

    # Direction: left to right = small to big
    # Finds smallest number to leftmost then it's counted as sorted
    for i in range(length):
        # Find smallest number from unsorted
        min_index = i
        for j in range(i + 1, length):
            if copied_list[min_index] > copied_list[j]:
                min_index = j

        # Swap found number
        copied_list[i], copied_list[min_index] = copied_list[min_index], copied_list[i]
    return copied_list


def insertion_sort(a_list):
    """
    Theoretical results (real life differ):
    Average case:   O(n^2)
    Best case:      O(n)
    Worst case:     O(n^2)
    """

    copied_list = a_list[:]
    length = len(a_list)

    # Direction: left to right = small to big
    # Leftmost considered sorted
    # Sort from index 1
    for i in range(1, length):
        # Select the current element
        key = copied_list[i] 

        # Shift key to the left
        j = i - 1
        while (j >= 0) and (key < copied_list[j]):
            copied_list[j + 1] = copied_list[j]
            j -= 1
        copied_list[j + 1] = key

    return copied_list


def merge_sort(a_list):
    """
    Theoretical results (real life differ):
    Average case:   O(n*log(n))
    Best case:      O(n*log(n))
    Worst case:     O(n*log(n))
    """

    copied_list = a_list[:]
        
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
    
    # Run the algorithm
    copied_list = merge_sort_recursion(copied_list)

    return copied_list


def quick_sort(a_list):
    """
    Theoretical results (real life differ):
    Average case:   O(n*log(n))
    Best case:      O(n*log(n))
    Worst case:     O(n^2)
    """

    copied_list = a_list[:]

    # Note: There are many ways to implement quick sort, and all using pivots.
    #       This one just targets a list instead of using one point and swapping it manually.
    # Direction: left to right = small to big
    def quick_sort_recursion(a_list):
        if len(a_list) <= 1:
            return a_list
        # In sorted: Left of pivot is smaller than pivot; Right of pivot is larger than pivot
        pivot = a_list[len(a_list) // 2]
        #print("PIVOT", pivot)
        left = [num for num in a_list if num < pivot]
        #print("Left:", left)
        # Middle is equal to pivot, it's just to make a list so it's easier to use concatenation.
        middle = [num for num in a_list if num == pivot] 
        #print("Mid:", middle) 
        right = [num for num in a_list if num > pivot]
        #print("Right:", right)
        return quick_sort_recursion(left) + middle + quick_sort_recursion(right)

    # Run the algorithm
    copied_list = quick_sort_recursion(copied_list)

    return copied_list


# OKAY... not understand yet (below)
def heap_sort(a_list):
    """
    Theoretical results (real life differ):
    Average case:   O(n*log(n))
    Best case:      O(n*log(n))
    Worst case:     O(n*log(n))
    """

    copied_list = a_list[:]
    
    def heapify(arr, n, i):
        """
        Turns list into heap.
        """
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is greater than root
        if l < n and arr[l] > arr[largest]:
            largest = l

        # See if right child of root exists and is greater than root or largest so far
        if r < n and arr[r] > arr[largest]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap

            # Heapify the root.
            heapify(arr, n, largest)

    # The main function to sort an array of size n
    def heapSort(arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            heapify(arr, i, 0)

    heapSort(copied_list)
    return copied_list