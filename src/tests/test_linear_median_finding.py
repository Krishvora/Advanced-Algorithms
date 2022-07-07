import unittest
import random
from algorithm import linear_median_finding 

class TestLinearMedianFinding(unittest.TestCase):
    accuracy = 0.6

    def test_linear_median_finding(self):
        for n in range(1, 100):
            seq = [i for i in range(n)]
            random.shuffle(seq)
            for k in range(n):
                for group_amount in (3, 5, 7):
                    passed = True
                    try:
                        index = linear_median_finding(seq, k, group_amount)
                        self.assertIn(index, range(len(seq)))
                    except Exception:
                        passed = False
                    self.assertTrue(passed)
    
    def test_accuracy(self):
        for length in range(1, 100):
            passed = False
            count = 0
            for group_amount in (3, 5, 7):
                for _ in range(1000):
                    seq = [i for i in range(length)]
                    random.shuffle(seq)
                    expected = len(seq) // 2
                    index = linear_median_finding(seq, expected, group_amount)
                    if seq[index] == expected:
                        passed = True
                    if abs(seq[index] - expected) < 3:
                        count += 1
                self.assertTrue(count / 100 >= self.accuracy)
                self.assertTrue(passed)

if __name__ == '__main__':
    unittest.main()