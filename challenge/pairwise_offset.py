from collections import deque


def pairwise_offset(sequence, fillvalue='*', offset=0):
    seq1, seq2 = deque(sequence), deque(sequence)
    for i in range(offset):
        seq2.appendleft(fillvalue)
        seq1.append(fillvalue)

    return list(zip(seq1, seq2))


