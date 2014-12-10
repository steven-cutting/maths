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
