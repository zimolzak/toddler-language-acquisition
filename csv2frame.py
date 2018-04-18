import pandas as pd
INPUT_FILENAME = 'day_per_row.csv'
LINES = open(INPUT_FILENAME, 'r').read().splitlines()
DATE_LIST = []
WORD_LIST = []
for L in LINES:
    line_list = L.split(',')
    for i in range(1,len(line_list)): # start w/ 1 not 0.
        DATE_LIST.append(line_list[0])
        WORD_LIST.append(line_list[i])

DF = pd.DataFrame({'date':DATE_LIST, 'word':WORD_LIST})
print(DF)
