from typing import List
from ...exceptions import InputError

def algorithm(seq: List[int], k: int, group_amount: int) -> int:
    if k > len(seq):
        raise InputError('k must less than the length of the input sequence')
    if len(seq) == 0:
        raise InputError('sequence cannot be empty')

    def select(seq: List[int], n: int, left: int=0, right: int=None) -> int:
        if not right:
            right = len(seq)
        while True:
            if left is right:
                return left
            pivotIndex = pivot(seq, left, right)
            pivotIndex = partition(seq, left, right, pivotIndex, n)
            if n == pivotIndex:
                return n
            elif n < pivotIndex:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1

    def partition(seq: List[int], left: int, right: int, pivotIndex: int, n: int) -> int:
        pivotValue = seq[pivotIndex]
        seq[pivotIndex], seq[right - 1] = seq[right - 1], seq[pivotIndex]
        storeIndex = left
        for i in range(left, right - 1):
            if seq[i] < pivotValue:
                seq[storeIndex], seq[i] = seq[i], seq[storeIndex]
                storeIndex += 1
        storeIndexEq = storeIndex
        for i in range(storeIndex, right - 1):
            if seq[i] is pivotValue:
                seq[storeIndexEq], seq[i] = seq[i], seq[storeIndexEq]
                storeIndexEq += 1
        seq[right - 1], seq[storeIndexEq] = seq[storeIndexEq], seq[right - 1]
        if n < storeIndex:
            return storeIndex
        if n <= storeIndexEq:
            return n
        return storeIndexEq
        
    def pivot(seq: List[int], left: int, right: int) -> int:
        if right - left < group_amount:
            return find_median_index(seq, left, right)
        
        for i in range(left, right, group_amount):
            subleft, subright = i, i+group_amount if i+group_amount <= len(seq) else len(seq)
            index = find_median_index(seq, subleft, subright)
            seq[index], seq[left+((i - left)//group_amount)] = seq[left+((i - left)//group_amount)], seq[index]
        
        mid = (right - left) // (2 * group_amount) + left
        return select(seq, mid, left, left + ((right - left) // group_amount))

    def find_median_index(seq: List[int], left: int, right: int) -> int:
        if right - left < 3:
            return right - 1

        less_index, mid_index, greater_index = sort_three_indice(seq, [left, left + 1, left + 2])

        if right - left == 3:
            return mid_index

        greater = [i for i in range(left+3, right) if seq[i] > seq[mid_index]]
        less = [i for i in range(left+3, right) if seq[i] < seq[mid_index]]

        if right - left <= 5:
            if right - left == 4:
                if greater:
                    greater.append(find_max_index(seq, greater))
                else:
                    less.append(find_min_index(seq, less))
            if len(greater) == 0:
                less.append(less_index)
                return find_max_index(seq, less)
            elif len(greater) == 1:
                return mid_index
            else:
                greater.append(greater_index)                
                return find_min_index(seq, greater)
        if right - left <= 7:
            if right - left == 6:
                if greater:
                    greater.append(find_max_index(seq, greater))
                else:
                    less.append(find_min_index(seq, less))
            if len(greater) == 0:
                less.append(less_index)
                index_too_large = find_max_index(seq, less)
                less = [num for num in less if num != index_too_large]
                return find_max_index(seq, less)
            elif len(greater) == 1:
                less.append(less_index)
                return find_max_index(seq, less)
            elif len(greater) == 2:
                return mid_index
            elif len(greater) == 3:
                greater.append(greater_index)
                return find_min_index(seq, greater)
            else:
                greater.append(greater_index)
                index_too_small = find_min_index(seq, greater)
                greater = [num for num in greater if num != index_too_small]
                return find_max_index(seq, greater)
        else:
            print([seq[i] for i in range(left, right)])
            raise Exception('Group amount not support')
    
    def sort_three_indice(seq: List[int], indice: List[int]) -> List[int]:
        assert len(indice) == 3
        for i in range(len(indice)):
            for j in range(i+1, len(indice)):
                if seq [indice[i]] > seq[indice[j]]:
                    indice[i], indice[j] = indice[j], indice[i]
        return indice
    
    def find_min_index(seq: List[int], indice: List[int]) -> int:
        return min([(index, seq[index]) for index in indice], key = lambda x: x[1])[0]
    
    def find_max_index(seq: List[int], indice: List[int]) -> int:
        return max([(index, seq[index]) for index in indice], key = lambda x: x[1])[0]

    index = select(seq, k)

    return index