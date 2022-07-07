import time
import json
from algorithm import quick_sort, init_seq, QuickSortMode

def lambda_handler(event, context):
    
    n = event['numberSequenceLength']
    modes = {
        'linearTimeGroupAmount3': event.get('linearTimeGroupAmount3'),
        'linearTimeGroupAmount5': event.get('linearTimeGroupAmount5'),
        'linearTimeGroupAmount7': event.get('linearTimeGroupAmount7'),
        'randomized': event.get('randomized'),
    }

    
    report = compute(n, modes)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'report': report,
            'params': event
        }),
    }

def compute(n: int, modes: dict):
    seq = init_seq(n)
    seqText = ','.join([str(num) for num in seq])

    results = {}

    mode_map = {
        'linearTimeGroupAmount3': QuickSortMode.LINEAR_3,
        'linearTimeGroupAmount5': QuickSortMode.LINEAR_5,
        'linearTimeGroupAmount7': QuickSortMode.LINEAR_7,
        'randomized': QuickSortMode.RANDOMIZED,
    }

    for mode in modes.keys():
        if modes.get(mode):
            sorted, delta_millisec = monitor(quick_sort, [seq.copy(), mode_map[mode]])
            results[mode] = {
                'time': delta_millisec,
            }
            
    return {
        'results': results,
        'seq': seqText,
    }


def monitor(func, args):    
    start_time = time.time()
    sorted = func(*args)
    end_time = time.time()

    delta_millisec = 1000 * (end_time - start_time)
    delta_millisec = f'{delta_millisec} milliseconds'
    
    return (sorted, delta_millisec)
