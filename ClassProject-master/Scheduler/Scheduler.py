__author__ = 'marcopereira'
import numpy as np
from dateutil.relativedelta import relativedelta
import pandas as pd


class Scheduler(object):
    def __init__(self):
        pass

    def getSchedule(self, start, end, freq):
        return pd.date_range(start=start,end=end,freq=freq).date

    def extractDelay(self, freq):
        if type(freq) == list:
            freq = freq[0]
        if (freq == 'Date'): return relativedelta(days=+  0)
        x = self.only_numerics(freq)
        if (x == ''):
            freqValue = 100
        else:
            freqValue = np.int(x)
        if (freq.upper().find('D') != -1): delta = relativedelta(days=+  freqValue)
        if (freq.upper().find('W') != -1): delta = relativedelta(weeks=+  freqValue)
        if (freq.find('M') != -1): delta = relativedelta(months=+ freqValue)
        if (freq.find('Y') != -1): delta = relativedelta(years=+ freqValue)
        if (freq.find('ZERO') != -1): delta = relativedelta(years=+ freqValue)
        return delta


    def only_numerics(self, seq):
        seq_type = type(seq)
        return seq_type().join(filter(seq_type.isdigit, seq))