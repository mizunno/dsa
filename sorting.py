

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

def merge_sort(elements):
    pass

def selection_sort(elements):
    pass

def insertion_sort(elements):
    pass

def quick_sort(elements):
    pass

