#import matplotlib.pyplot as plt
INPUT_FILENAME = 'day_per_row.csv'

def filename2frame(fn):
    """Make two lists a shorthand CSV.

    In other words, unroll the CSV. It's a slightly unusual CSV in
    that column 0 is always a date, and then there are a *variable*
    number of subsequent columns that you can think of as word0,
    word1, ... wordn. This compact / rolled-up structure simply allows
    me to type the CSV faster.
    """
    rows = open(fn, 'r').read().splitlines()
    date_list = []
    word_list = []
    for r in rows:
        columns = r.split(',')
        # Assume columns[0] is always date and columns[1..end] are words.
        for i in range(1,len(columns)):
            if columns[i] not in word_list: # dedup assumes CSV chronological.
                date_list.append(columns[0])
                word_list.append(columns[i])
    return date_list, word_list

(D, W) = filename2frame(INPUT_FILENAME)

for (di, wi) in zip(D, W):
    print(wi, di)
