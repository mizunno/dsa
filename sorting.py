

def bubble_sort(elements):
    """
    Sorts a list using the Bubble Sorting algorithm.
    (https://www.programiz.com/dsa/bubble-sort)
    """
    for i in range(0, len(elements) - 1):

        # track if swapping
        swapped = False

        for j in range(0, len(elements) - i - 1):

            # if next element is lower than the current one, swap them
            if elements[j + 1] < elements[j]:
                elements[j + 1], elements[j] = elements[j], elements[j + 1]
                swapped = True

        # if no swap was made, the list is already sorted,
        # so we avoid further comparison
        if not swapped:
            break

    return elements


def insertion_sort(elements):
    """
    Sorts a list using the Insertion Sort algorithm.
    (https://www.programiz.com/dsa/insertion-sort)
    """
    for i in range(1, len(elements)):

        # sort one item at a time
        j = i 

        # keep swapping until the item is sort or at the first position
        while j > 0 and elements[j - 1] > elements[j]:
            elements[j - 1], elements[j] = elements[j], elements[j - 1]
            j -= 1
    
    return elements


def selection_sort(elements):
    """
    Sort a list using the Selection Sort algorithm.
    (https://www.programiz.com/dsa/selection-sort)
    """

    for i in range(len(elements)):
        smallest_idx = i

        # search for the smallest idx
        for j in range(smallest_idx + 1, len(elements)):
            if elements[j] < elements[smallest_idx]:
                smallest_idx = j

        elements[smallest_idx], elements[i] = elements[i], elements[smallest_idx]

    return elements


def merge_sort(elements):

    """
    Sort a list using the Merge Sort algorithm. It is
    a Divide and Conquer algorithm.
    - Divide: divides the list into sublists.
    - Conquer: merges sublists while sorting the elements.
    (https://www.programiz.com/dsa/merge-sort)
    """

    # Base case: return the input if the list has one element
    if len(elements) <= 1:
        return elements
    
    # Divide the list into two sublists
    mid = len(elements) // 2
    left, right = elements[:mid], elements[mid:]

    # Recursive calls to continue dividing the list until reaching the 
    # base case
    left = merge_sort(left)
    right = merge_sort(right)


    # Merge phase: merge both lists into one final list while sorting 
    # their elements
    left_idx, right_idx = 0, 0
    merged = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx+=1
        else:
            merged.append(right[right_idx])
            right_idx+=1

    
    # Append remaining elements from the left sublist
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx+=1;

    # Append remaining elements from the right sublist
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx+=1;

    return merged
