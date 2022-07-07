import unittest
import json
from lambda_functions.median_finding.lambda_function import lambda_handler as median_finding
from lambda_functions.quick_sort.lambda_function import lambda_handler as quick_sort

class TestLambdaFunctions(unittest.TestCase):
    
    def test_median_finding(self):
        modes = [
            'linearTimeGroupAmount3',
            'linearTimeGroupAmount5',
            'linearTimeGroupAmount7',
            'randomized'
        ]

        for n in range(1, 100):
            for k in range(n):
                event = {
                    'numberSequenceLength': n,
                    'targetNumber': k,
                    'linearTimeGroupAmount3': True,
                    'linearTimeGroupAmount5': True,
                    'linearTimeGroupAmount7': True,
                    'randomized': True,
                }
                response = median_finding(event, {})
                body = response.get('body')
                body = json.loads(body)
                params = body.get('params')
                report = body.get('report')
                results = report.get('results')

                self.assertEqual(params, event)

                for mode in modes:
                    result = results.get(mode)
                    self.assertIn('time', result)
                    self.assertIn('found_number', result)

                self.assertIn('seq', report)
                self.assertIn('target_number', report)
    
    def test_quick_sort(self):
        modes = [
            'linearTimeGroupAmount3',
            'linearTimeGroupAmount5',
            'linearTimeGroupAmount7',
            'randomized'
        ]

        for n in range(1, 100):
            event = {
                'numberSequenceLength': n,
                'linearTimeGroupAmount3': True,
                'linearTimeGroupAmount5': True,
                'linearTimeGroupAmount7': True,
                'randomized': True,
            }
            response = quick_sort(event, {})
            body = response.get('body')
            body = json.loads(body)
            params = body.get('params')
            report = body.get('report')
            results = report.get('results')

            self.assertEqual(params, event)

            for mode in modes:
                result = results.get(mode)
                self.assertIn('time', result)

            self.assertIn('seq', report)

if __name__ == '__main__':
    unittest.main()