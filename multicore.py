from __future__ import division
__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/25/2014'


if __name__ == "__main__":

    import math
    import cmath
    import sys
    import platform
    from decimal import Decimal

    import maths
    import maths.tests.wallis.wallistests as wtests
    from maths import generalfunctions as gfunc

    import logging
    logging.basicConfig(filename='data/logs/mulicore.log', level=logging.INFO)
    LOG = logging.getLogger(__name__)

    prossesors_list = gfunc.cpu_info()

    info = {'script' : sys.argv[0],
            'host' : platform.uname()[1],
            'architecture' : platform.uname()[4],
            'cpuinfo' : prossesors_list[0],
            'cores' : len(prossesors_list),
            'implementation' : platform.python_implementation(),
            'cores_used' : int(sys.argv[1]),
            'i' : int(sys.argv[2]),
            'processes' : gfunc.processes_running(),
            'repeat' : 2,
            'number' : 3,
            }

    with gfunc.Timer() as timer_:
        final_pi = maths.para_wallis(info['i'], info['cores_used'])

    info['pi'] = Decimal(final_pi)
    info['runtime'] = timer_.interval

    logger_str1 = """script
        architecture
        cpuinfo
        cores
        processes
        implementation
        cores_used
        i
        pi
        runtime""".replace('\n' + ' '*8, '\t')
    lables = 'log\t'+logger_str1
    log_str = ''.join(['\t{', logger_str1.replace('\t', '}\t{'), '}']).format(**info)

    #LOG.info(lables)
    LOG.info(log_str)

    #logger_str = """log script host cores_used processes_running i time pi""".replace(' ', '\t')
    #LOG.info(logger_str)
