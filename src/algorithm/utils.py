import random

def init_seq(n):
    seq = [i for i in range(n)]
    random.shuffle(seq)
    return seq