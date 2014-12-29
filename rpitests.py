from __future__ import division

__title__ = 'maths'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'



if __name__ == "__main__":

    import math
    import cmath
    import sys
    import platform
    from decimal import Decimal

    from maths import generalfunctions as gfunc

    import maths
    import maths.tests.wallis.wallistests as wtests

    import logging
    logging.basicConfig(filename='data/logs/rpitests.log', level=logging.INFO)
    LOG = logging.getLogger(__name__)

    script = sys.argv[0]
    arg = sys.argv[1]
    i = int(sys.argv[2])
    processes = gfunc.processes_running()

    with gfunc.Timer() as timer:

        i = int(sys.argv[2])
        arg = sys.argv[1]

        if arg == 'std':
            pie, i = maths.wallis(i)
        elif arg == 'gen':
            pie, i = maths.wallisgen(i)

    worktime = timer.interval
    pi = Decimal(pie)


    logger_str1 = """
        script={script}
        function={arg}
        host={host}
        cores_used={cores}
        processes_running={procs}
        i={i}
        time={worktime}
        pi={pi}""".format(script=script,
                          arg=arg,
                          host=platform.uname()[1],
                          cores=1,
                          procs=processes,
                          i=i,
                          worktime=worktime,
                          pi=pi).replace(' '*8, '\t')

    logger_str = """
        {script}
        {arg}
        {host}
        {cores}
        {procs}
        {i}
        {worktime}
        {pi}""".format(script=script,
                       arg=arg,
                       host=platform.uname()[1],
                       cores=1,
                       procs=processes,
                       i=i,
                       worktime=worktime,
                       pi=pi).replace('\n' + ' '*8, '\t')

    LOG.info(logger_str)
