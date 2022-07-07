import unittest
import random
from algorithm import randomized_median_finding 

class TestRandomizedMedianFinding(unittest.TestCase):
    accuracy = 0.6
    
    def test_randomized_median_finding(self):
        for n in range(1, 100):
            seq = [i for i in range(n)]
            random.shuffle(seq)
            passed = True
            try:
                index = randomized_median_finding(seq)
                self.assertIn(index, range(len(seq)))
            except Exception:
                passed = False
            self.assertTrue(passed)
    
    def test_accuracy(self):
        for length in range(30, 100):
            count = 0
            for _ in range(1000):
                seq = [i for i in range(length)]
                random.shuffle(seq)
                expected = len(seq) // 2
                index = randomized_median_finding(seq)
                stdv = (sum([(num - expected) ** 2 for num in seq]) / length) ** (1/2)
                if abs(seq[index] - expected) <= stdv:
                    count += 1
            self.assertTrue(count / 100 >= self.accuracy, (count / 100, length))

if __name__ == '__main__':
    unittest.main()