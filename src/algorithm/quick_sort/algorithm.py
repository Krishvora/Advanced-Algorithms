from enum import Enum
from algorithm import linear_median_finding, randomized_median_finding

class Mode(Enum):
    LINEAR_3 = lambda seq : linear_median_finding(seq, len(seq) // 2, 3)
    LINEAR_5 = lambda seq : linear_median_finding(seq, len(seq) // 2, 5)
    LINEAR_7 = lambda seq : linear_median_finding(seq, len(seq) // 2, 7)
    RANDOMIZED = lambda seq : randomized_median_finding(seq)
    def __init__(self, func):
        self.func = func

def algorithm(seq: list, mode: Mode=Mode.LINEAR_5):
    return quick_sort(seq, mode)
      
def quick_sort(array: list, mode: Mode):

    queue = [(0, len(array) - 1)]

    while queue:
        (start, end) = queue.pop()
        if (start < end):          
            p = partition(start, end, array, mode)
            queue.append((start, p - 1))
            queue.append((p + 1, end))
    
    return array

def partition(start: int, end: int, array: list, mode: Mode):
    
    pivot_index = mode(array[start:end + 1]) + start
    array[start], array[pivot_index] = array[pivot_index], array[start]

    pivot_index = start
    pivot = array[pivot_index]
      
    while start < end:
          
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        while array[end] > pivot:
            end -= 1
          
        if start < end:
            array[start], array[end] = array[end], array[start]
    
    if end > pivot_index and array[end] < array[pivot_index]:
        array[end], array[pivot_index] = array[pivot_index], array[end]
     
    return end