"""This module provides a insertion sort algorithm."""


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the insertion sort algorithm.

    This algorithm iterates over the list, and for each element, compares it with the
    previous elements, shifting them as needed to ensure the current element is
    inserted in the correct position. It continues this process until the entire
    list is sorted.

    Args:
        list (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers.
    """
    for i in range(1, len(arr)):
        while i > 0:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
            else:
                break
    return arr


list = [7, 3, 1, 6, 4, 2]
print(*insertion_sort(list), sep=", ")
