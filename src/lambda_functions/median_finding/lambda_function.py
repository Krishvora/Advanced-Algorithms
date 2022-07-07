import time
import json
from algorithm import randomized_median_finding, linear_median_finding, init_seq

def lambda_handler(event, context):

    n = event.get('numberSequenceLength')
    modes = {
        'linearTimeGroupAmount3': event.get('linearTimeGroupAmount3'),
        'linearTimeGroupAmount5': event.get('linearTimeGroupAmount5'),
        'linearTimeGroupAmount7': event.get('linearTimeGroupAmount7'),
        'randomized': event.get('randomized'),
    }
    target_number = event.get('targetNumber')
    
    report = compute(n, target_number, modes)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'report': report,
            'params': event
        }),
    }

def compute(n: int, target_number: int, modes: dict):
    seq = init_seq(n)

    results = {}

    func_args_map = {
        'linearTimeGroupAmount3': (linear_median_finding, [seq, target_number, 3]),
        'linearTimeGroupAmount5': (linear_median_finding, [seq, target_number, 5]),
        'linearTimeGroupAmount7': (linear_median_finding, [seq, target_number, 7]),
        'randomized': (randomized_median_finding, [seq]),
    }

    for mode in modes.keys():
        if modes.get(mode):
            func, args = func_args_map[mode]
            index, delta_millisec = monitor(func, args)
            found_number = seq[index]
            results[mode] = {
                'time': delta_millisec,
                'found_number': found_number
            }

    seq = ','.join([str(num) for num in seq])

    return {
        'results': results,
        'seq': seq,
        'target_number': target_number,
    }


def monitor(func, args):    
    start_time = time.time()
    index = func(*args)
    end_time = time.time()

    delta_millisec = 1000 * (end_time - start_time)    
    delta_millisec = f'{delta_millisec} milliseconds'
    
    return (index, delta_millisec)
