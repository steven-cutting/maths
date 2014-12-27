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

    script = sys.argv[0]
    cores = int(sys.argv[1])
    i = int(sys.argv[2])
    processes = gfunc.processes_running()

    with gfunc.Timer() as timer:
        final_pi = maths.para_wallis(i, cores)

    worktime = timer.interval
    pi = Decimal(final_pi)

    logger_str = """
        {script}
        {host}
        {cores}
        {procs}
        {i}
        {worktime}
        {pi}""".format(script=script,
                       host=platform.uname()[1],
                       cores=cores,
                       procs=processes,
                       i=i,
                       worktime=worktime,
                       pi=pi).replace('\n' + ' '*8, '\t')

    #logger_str = """log script host cores_used processes_running i time pi""".replace(' ', '\t')
    LOG.info(logger_str)
