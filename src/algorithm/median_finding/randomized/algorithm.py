from algorithm.exceptions import InputError
import random

def algorithm(seq: list):
    if len(seq) == 0:
        raise InputError
    population_amount = int(len(seq) ** (3/4))
    sub_seq = set()
    for _ in range(population_amount):
        index = random.randint(0, len(seq) - 1)
        sub_seq.add(seq[index])
    sub_seq = list(sub_seq)
    for i in range(len(sub_seq)):
        for j in range(i+1, len(sub_seq)):
            if sub_seq[i] > sub_seq[j]:
                sub_seq[i], sub_seq[j] = sub_seq[j], sub_seq[i]
    index = seq.index(sub_seq[len(sub_seq) // 2])    
    return index