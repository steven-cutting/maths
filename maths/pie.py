__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'

from __future__ import division
import math
import cmath
import sys
from decimal import Decimal
from itertools import islice, count, izip, imap, product, chain

# The basic equation:
# pi = ((4 * (i**2))/((4 * (i**2)) - 1)) * pi
# pi = ((4 *    a  )/((4 *   a   ) - 1)) * pi
# pi = (      b     /(      b      - 1)) * pi
# pi = (      b     /          c       ) * pi
# pi =              d                    * pi
# a = i**2
# b = 4 * a
# c = b - 1
# d = b / c
# pi = d * pi


def wallis_equation(i):
    # This replaces this: ((4.0*(i**2.0))/((4.0*(i**2.0))-1.0))
    # Reduces redundant operations.
    a = i**2
    b = 4*a
    c = b - 1
    return b / c


def wallis(stop, start=0, pie=1):
    pi = pie
    end = stop - start
    iteration = 0
    try:
        for i,v in enumerate(imap(wallis_equation, islice(count(start + 1), 0, end))):
            p = pi
            pi = v * p
            iteration = i
    except KeyboardInterrupt:
        return pi * 2, iteration
    return pi * 2, iteration


def wallisgen(stop, start=0, pie=1):
    pi = pie
    end = stop - start
    for i in islice(count(start + 1), 0, end):
        v = wallis_equation(i)
        p = pi
        pi = v * p
    return pi * 2
# think about implementing product() form itertools.
# If I split up large values of i into multiple iterables use chain() form itertools.


def genmill(stop, start=0):
    # exclusive
    end = stop - start
    return islice(count(start), 0, end)


# ------------------------------------------------------------------------------
# **Depreciated**
# This code is from when I first stared learning python, so it is very bad.
# Only here for comparison.

def P_Pie(base, amount, pies):
	# terst = 0
	for i in xrange(base, amount+1):
		pies = ((4.0*(i**2.0))/((4.0*(i**2.0))-1.0))*pies
		# terst += 1
	# print "------"
	# print terst
	# print "------"
	return pies


def wallisold(num):
	pie = 1.0
	for i in islice(count(1), int(num)):
		pie = ((4.0*(i**2.0))/((4.0*(i**2.0))-1.0))*pie
	return 2*pie





def wallis2(num):
	s = 4
	# print s
	end = int(num/s)
	numo = int(num/s)
	numi = int(num/s)*(s-1)
	start = 1
	pie = 1.0
	# print [1, end, numo, numi, start, pie]

	for times in range(1, s):
		# print ['p', times, end, start]
		start = (end + 1) - numo

		if times == 1:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]

		else:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]

	# print [2, end, numo, numi, start, pie]

	start = (end + 1) - numo

	while (numi + numo) != num:
		numo += 1

	# print [3, end, numo, numi, start, pie]

	pie = P_Pie(start, numo + numi, pie)

	# print [4, end, numo, numi, start, pie]

	return 2*pie




def wallis3(num):
	splits = (lambda x: (int(math.sqrt(math.sqrt(x))) if x>1000000 else 4))
	s = splits(num)
	# print s
	end = int(num/s)
	numo = int(num/s)
	numi = int(num/s)*(s-1)
	start = 1
	pie = 1.0
	# print [1, end, numo, numi, start, pie]

	for times in range(1, s):
		# print ['p', times, end, start]
		start = (end + 1) - numo

		if times == 1:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]

		else:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]

	# print [2, end, numo, numi, start, pie]

	start = (end + 1) - numo

	while (numi + numo) != num:
		numo += 1

	# print [3, end, numo, numi, start, pie]

	pie = P_Pie(start, numo + numi, pie)

	# print [4, end, numo, numi, start, pie]

	return 2*pie





def wallis4(num):
    pies = []
    for i in islice(count(1), int(num)):
        pies.append((4.0*(i**2.0))/((4.0*(i**2.0))-1.0))

    pie = 1

    for seq in pies:
        pie *= seq

    return pie*2


def trip(a, b):
    return a/b



def wallis5(num):
    i2 = []
    fouri2 = []
    btm = []
    pies = []
    pie = 1

    for i in islice(count(1), int(num)):
        i2.append(i**2.0)

    for seq in i2:
        fouri2.append(seq*4.0)

    for seq in fouri2:
        btm.append(seq-1.0)

    for seq,point in izip(btm,fouri2):
        pies.append(point/seq)

    for seq in pies:
        pie *= seq

    return pie*2






