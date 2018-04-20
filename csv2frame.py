# If you want the boxplots (pandas + matplotlib)
# source activate py27
# pythonw csv2frame.py

import pandas as pd
# import matplotlib.pyplot as plt
INPUT_FILENAME = 'day_per_row.csv'

def filename2frame(fn):
    """Make a pandas DataFrame from a shorthand CSV.

    In other words, unroll the CSV into a DataFrame. It's a slightly
    unusual CSV in that column 0 is always a date, and then there are
    a *variable* number of subsequent columns that you can think of as
    word0, word1, ... wordn. This compact / rolled-up structure simply
    allows me to type the CSV faster.
    """
    rows = open(fn, 'r').read().splitlines()
    date_list = []
    word_list = []
    for r in rows:
        columns = r.split(',')
        # Assume columns[0] is always date and columns[1..end] are words.
        for i in range(1,len(columns)):
            date_list.append(columns[0])
            word_list.append(columns[i])
    return pd.DataFrame({'date':date_list, 'word':word_list})

D = filename2frame(INPUT_FILENAME)

# E = pd.DataFrame({'c1':[1,2,3,4,5,3,3,2],
#                  'c2':[2,2,3,3,4,9,2,1]})
# E.boxplot()
# plt.show()

#print(D.sort('word')) # pandas 0.14.1
print(D)
print()
print(D.describe())
