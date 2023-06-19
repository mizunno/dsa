

def bubble_sort(elements):
    for i in range(1, len(elements)):
        j = i        
        while elements[j - 1] > elements[j] and j > 0:
            elements[j - 1], elements[j] = elements[j], elements[j - 1]
            j-=1

    return elements

def merge_sort(elements):
    pass

def selection_sort(elements):
    pass

def insertion_sort(elements):
    pass

def quick_sort(elements):
    pass

