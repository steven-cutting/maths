__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/25/2014'


import time
import pandas as pd

import logging
_LOG = logging.getLogger(__name__)


class Timer:
    def __init__(self):
        self.interval = 0
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

def buildsetof_N(N):
    if N % 10:
        n = N - (N % 10 - 10)
    else:
        n = N

    N_list = [n]
    while n >= 10:
        other_n = n // 10
        N_list.append(other_n)
        n = other_n
    return N_list

class bench(object):

    def __init__(self, function, N):
        self.N = N
        self.function = function
        self.N_list, self.times = self.timeforrange_n(self.function, self.N)

        self.dataframe = pd.DataFrame({'N': self.N_list,
                                       'Time': self.times})

    def __str__(self):
        n_just = max(map(len, map(str, self.N_list))) + 1
        t_just = max(map(len, map(str, self.times)))
        lines = [''.join(['N'.ljust(n_just), 'Time'.ljust(t_just)])]
        for n, time in zip(self.N_list, self.times):
            line = ''.join([str(n).ljust(n_just), str(time).ljust(t_just)])
            if type(line) is str:
                lines.append(line)
        return '\n'.join(lines)

        #return str([self.times, self.N_list])


    def timeforrange_n(self, function, N):
        times = []
        N_list = buildsetof_N(N)

        for n in N_list:
            with Timer() as t:
                function(n)
            times.append(t.interval)

        return N_list[::-1], times[::-1]


def multitime(function, N, times_to_run):
    n = N
    init = bench(function, n)
    fulltable = init.dataframe.set_index('N')
    iterations = times_to_run - 1
    for i in xrange(iterations):
        table = i + 2
        lable = 'Time{}'.format(table)
        newinst = bench(function, n)
        newtable = newinst.dataframe
        series = newtable['Time']
        print series
        fulltable[lable] = series
        print fulltable

    return fulltable
