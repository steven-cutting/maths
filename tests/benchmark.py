


class Timer:
    def __init__(self):
        self.interval = 0
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


def timeforrange_n(functiontuple, )
