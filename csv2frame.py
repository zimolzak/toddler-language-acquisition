import pandas as pd
INPUT_FILENAME = 'day_per_row.csv'

def filename2frame(fn):
    lines = open(fn, 'r').read().splitlines()
    date_list = []
    word_list = []
    for L in lines:
        line_list = L.split(',')
        for i in range(1,len(line_list)): # start w/ 1 not 0.
            date_list.append(line_list[0])
            word_list.append(line_list[i])
    return pd.DataFrame({'date':date_list, 'word':word_list})

print(filename2frame(INPUT_FILENAME))
