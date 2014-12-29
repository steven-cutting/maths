from __future__ import division
__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/28/2014'


if __name__ == "__main__":
    from timeit import Timer, timeit, repeat

    import math
    import cmath
    import sys
    import platform

    from decimal import Decimal

    import maths
    import maths.tests.wallis.wallistests as wtests
    from maths import generalfunctions as gfunc

    import logging
    logging.basicConfig(filename='data/logs/mulicore-bench.log', level=logging.INFO)
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


    cmd_str = "maths.para_wallis({i}, {cores_used})".format(**info)

    with gfunc.Timer() as timer_:
        Repeat = repeat(cmd_str,
                        setup="import maths",
                        repeat=info['repeat'],
                        number=info['number'])
    info['avg_time'] = sum(Repeat) / float(len(Repeat))
    info['runtime'] = timer_.interval

    logger_str1 = """script
        architecture
        cpuinfo
        cores
        processes
        implementation
        cores_used
        i
        repeat
        number
        avg_time
        runtime""".replace('\n' + ' '*8, '\t')
    lables = 'log\t'+logger_str1
    log_str = ''.join(['\t{', logger_str1.replace('\t', '}\t{'), '}']).format(**info)

    # LOG.info(lables)
    LOG.info(log_str)
