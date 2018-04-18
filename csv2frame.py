import pandas as pd
lines = open('day_per_row.csv', 'r').read().splitlines()
date_list = []
word_list = []
for L in lines:
    line_list = L.split(',')
    for i in range(1,len(line_list)): # start w/ 1 not 0.
        date_list.append(line_list[0])
        word_list.append(line_list[i])
print(date_list)
print(word_list)
