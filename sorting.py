

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
