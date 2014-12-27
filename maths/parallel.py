from __future__ import division
__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/26/2014'

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


def para_wallis(i, cores=1):

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
    results = pool.map(maths.wallis_parallel, kargs_to_map)

    product = reduce(mul, results, 1)

    final_pi = product * 2
    return final_pi
