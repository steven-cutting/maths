__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


from pie import wallis
import arrow

i = 1000000000000

t1 = arrow.now()

pies = wallis(i)

t2 = arrow.now()

print i
print pies
print 'time:'
print t2 - t1
