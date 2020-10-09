"""
Homegrown timing tools for function calls.
Does total time, best-of time and best-of-totals time
"""

import time
import sys

if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Return (total time, last result)
    """
    replist = list(range(reps))  # Hoist out, eqvalize 2.x, 3.x
    start = timer()
    for i in replist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Return (best time, last result)
    """
    best = 2 ** 32  # 136 years seems large enough
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)



def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    It will give best of total:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
