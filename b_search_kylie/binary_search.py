import random
import time


def naive_search(l, target):
    """
    Perform a naive linear search to find the target element in the given list.

    Parameters:
        l (list): The list in which to search for the target.
        target: The target element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    """
    Perform a binary search to find the target element in the given sorted list.

    Parameters:
        l (list): The sorted list in which to search for the target.
        target: The target element to search for.
        low (int): The lowest index of the sublist being searched (default is None).
        high (int): The highest index of the sublist being searched (default is None).

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    # Uncomment the following lines for testing individual search functions
    # l = [1, 2, 3, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print('Naive search time: ', (end - start)/length, 'seconds')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('Binary search time: ', (end - start)/length, 'seconds')
