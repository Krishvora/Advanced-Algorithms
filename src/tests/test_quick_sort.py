import unittest
import random
from algorithm import quick_sort, QuickSortMode

class TestQuickSort(unittest.TestCase):
    
    def test_quick_sort(self):
        for n in range(1, 100):
            for mode in QuickSortMode:
                seq = [i for i in range(n)]
                random.shuffle(seq)
                result = quick_sort(seq, mode)
                self.assertTrue(
                    all(
                        [result[i-1] < result[i] for i in range(1, len(result))]
                    ),
                    f'After sorting: {result}'
                )

if __name__ == '__main__':
    unittest.main()