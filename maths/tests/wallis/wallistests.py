# -*- coding: utf-8 -*-
__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


def wallisrun(equation, ilist):
    w = equation
    results = []

    for i in ilist:
        results.append(w(i))

    return results



    """ Will remove idea was dumb.
    options = [w(9),
               w(77),
               w(99999),
               w(69855),
               w(1000000),
               w(9999999),
               w(7750573),
               w(99999999),
               w(78365986),
               w(100000000),
               w(999999999),
               w(768956982),
              ]
    """
