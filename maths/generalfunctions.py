__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/25/2014'

import os
"""
try:
    import arrow
    CURRENT = arrow.now
except (ImportError):
    import time
    CURRENT = time.time
"""
import time
CURRENT = time.time

class Timer:
    def __init__(self):
        self.interval = 0
    def __enter__(self):
        # self.start = time.clock()
        self.start = CURRENT()
        return self

    def __exit__(self, *args):
        # self.end = time.clock()
        self.end = CURRENT()
        self.interval = self.end - self.start


def processes_running():
    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)

    return len(pids)

def cpu_info():
    prossesors_list = []
    with open('/proc/cpuinfo') as f:
        for line in f:
            # Ignore the blank line separating the information between
            # details about two processing units
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    prossesors_list.append(model_name)
    return prossesors_list
