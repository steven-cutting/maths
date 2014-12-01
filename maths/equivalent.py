# -*- coding: utf-8 -*-
from pie import wallis, wallis2, wallis3, wallis4, wallis5


a1 = wallis(9)
a2 = wallis(77)
a3 = wallis(99999)
a4 = wallis(11111111)
a5 = wallis(10000000)

b1 = wallis2(9)
b2 = wallis2(77)
b3 = wallis2(99999)
b4 = wallis2(11111111)
b5 = wallis2(10000000)

c1 = wallis3(9)
c2 = wallis3(77)
c3 = wallis3(99999)
c4 = wallis3(11111111)
c5 = wallis3(10000000)

d1 = wallis4(9)
d2 = wallis4(77)
d3 = wallis4(99999)
d4 = wallis4(11111111)
d5 = wallis4(10000000)

e1 = wallis5(9)
e2 = wallis5(77)
e3 = wallis5(99999)
e4 = wallis5(11111111)
e5 = wallis5(10000000)

print a1 == b1
print a2 == b2
print a3 == b3
print a4 == b4
print a5 == b5

print '-----------'

print a1 == c1
print a2 == c2
print a3 == c3
print a4 == c4
print a5 == c5

print '-----------'

print b1 == c1
print b2 == c2
print b3 == c3
print b4 == c4
print b5 == c5

print '-----------'

print a1 == d1
print a2 == d2
print a3 == d3
print a4 == d4
print a5 == d5

print '-----------'

print a1 == e1
print a2 == e2
print a3 == e3
print a4 == e4
print a5 == e5

print '-----------'




