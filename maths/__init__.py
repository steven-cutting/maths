__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


from .pie import wallis_equation, genmill, wallis, wallisgen, wallis_parallel
from parallel import para_wallis
