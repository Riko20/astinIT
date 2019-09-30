import time
import threading
import pandas as pd
import numpy as np
from pandas import DataFrame, Series


# 3 Create an object that has functions and members, that upon initiation produces random price data for 5 imaginary timeseries.
# Random numbers can be normal or uniform. The object should upon initiation start producing these numbers with one number being
# produced every second for each timeseries. The object should automatically save them in an efficient way (for example queues,dictionaries, pandas dataframe etc..) .
# The object
# should have the following functions (you can decide what members and internal structures you create to implement them in a functional way. )
# Function Start: when start is called the generation of data is started (and the data saved in the internal structures that you decide upon.

# Function returnLast: returns a dictionary with the names of the 5 imaginary timeseries as key and the last generated price values as values.
# Function maxLast20: returns a dictionary with the names of the 5 imaginary timeseries as keys and the maximum of the last 20 generated prices for each series as values.


def random_int_list(start, end, count):
    return np.random.randint(start, end, count)

def push_back_random_list(data_frame):
    data_frame.loc[len(data_frame)] = random_int_list(0, 10000, len(data_frame.columns))



class RandPrice:

    def __init__(self):
        timeseries = pd.date_range("2018-07-24", "2018-07-28")
        self.df = pd.DataFrame(columns=timeseries)
        push_back_random_list(self.df)
        self._th = threading.Thread(target = self._simulateIncomeData, args = (self.df,), daemon=True)

    def _simulateIncomeData(self, data_frame):
        while True:
            push_back_random_list(data_frame)
            print("Fil with len {}".format(len(data_frame)))
            time.sleep(1)

    def start(self):
        self._th.start()


    def returnLast(self, num_of_last):
        last_df = self.df.tail(num_of_last)
        last_dict = last_df.to_dict('list')
        return last_dict

    def returnMax(self, num_of_last):
        last_dict = self.returnLast(num_of_last)
        max_df = DataFrame(last_dict).max(axis=0)
        max_dict = max_df.to_dict()
        return max_dict


rnd = RandPrice()
rnd.start()
time.sleep(22)

print(rnd.returnLast(2))
print(rnd.returnMax(20))
print(rnd.df)
