from __future__ import division
import math
import cmath
import sys
from decimal import Decimal

#import pie
pistr = '3.141592653589793115997963468544'
pi = 3.141592653589793115997963468544

print 'str:\n', pistr
print 'float:\n', pi
print 'decimal:\n',Decimal(math.pi)
print 'mathpi:\n%.48f' % math.pi


if __name__ == "__main__":
    print int(sys.argv[1])

