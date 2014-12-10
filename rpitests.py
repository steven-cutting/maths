from __future__ import division
import math
import cmath
import sys
from decimal import Decimal
import arrow


import maths
import tests.wallis.wallistests as wtests

"""
print maths.wallis_equation(1)
print maths.oldeq(1)
print maths.wallis_equation(2)
print maths.oldeq(2)
print maths.wallis_equation(1000)
print maths.oldeq(1000)
print maths.wallis_equation(10000)
print maths.oldeq(10000)


g = maths.genmill(start=20, stop=25)
for i in g:
    print i
"""
"""
pistr = '3.141592653589793115997963468544'
pi = 3.141592653589793115997963468544

print 'str:\n', pistr
print 'float:\n', pi
print 'decimal:\n',Decimal(math.pi)
print 'mathpi:\n%.48f' % math.pi

print '\n\n'
"""
i = int(sys.argv[2])
arg = sys.argv[1]

if arg == 'std':
    print 'std:'
    print Decimal(maths.wallis(i))
elif arg == 'gen':
    print 'gen:'
    print Decimal(maths.wallisgen(i))


#print maths.wallis(1)

if __name__ == "__main__":
    print sys.argv
