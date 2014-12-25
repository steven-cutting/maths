__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


if __name__ == "__main__":
    from __future__ import division
    import math
    import cmath
    import sys
    from decimal import Decimal


    import maths
    import tests.wallis.wallistests as wtests

    import logging
    _LOG = logging.getLogger(__name__)


    print sys.argv

    i = int(sys.argv[2])
    arg = sys.argv[1]

    if arg == 'std':
        print 'std:'
        pie, i = maths.wallis(i)
        print "\ni = {}\npi = {}".format(i, Decimal(pie))
    elif arg == 'gen':
        print 'gen:'
        pie, i = maths.wallisgen(i)
        print "\ni = {}\npi = {}".format(i, Decimal(pie))

