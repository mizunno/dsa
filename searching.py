

def linear_search(elements, target):
    """
    Search the target in the elements list using
    the Linear Search algorithm.
    """

    for e in elements:
        if e == target:
            return True
        
    return False

def binary_search(elements, target):
    """
    Search the target in the elements list using
    the Binary Search algorithm.
    It requires the list to be sorted.
    """
    
    low, high = 0, len(elements) - 1

    while low <= high:
        
        mid = (low + high) // 2

        if elements[mid] == target:
            return True
        
        if target < elements[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False