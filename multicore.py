__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


if __name__ == "__main__":
    #from __future__ import division
    import math
    import cmath
    import sys
    from decimal import Decimal

    from operator import mul

    from multiprocessing import Pool

    import maths
    import maths.tests.wallis.wallistests as wtests
    from maths import generalfunctions as gfunc

    import logging
    _LOG = logging.getLogger(__name__)

    print sys.argv

    with gfunc.Timer() as timer:
        i = int(sys.argv[2])
        cores = int(sys.argv[1])

        kargs_to_map = []
        for number in xrange(cores):
            num = number + 1
            kargs_to_map.append({'stop' : i,
                                'start' : num,
                                'step' : cores,
                                })

        #for karg in tuple(kargs_to_map):
        #    maths.wallis_parallel(karg)

        pool = Pool(processes=cores)
        results = pool.map(maths.wallis_parallel, tuple(kargs_to_map))

        product = reduce(mul, results, 1)

        final_pi = product * 2
        print final_pi

    print timer.interval

