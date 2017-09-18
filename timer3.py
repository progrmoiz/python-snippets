# File timer3.py
"""
Same usage as timer2.py, but uses 3.x keyword-only default arguments
istead of dict pops for simpler code. No need to hoist range() out of tests
in 3.x: always a generator in 3.x, and this can't run on 2.x
"""

import time
import sys

if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(func, *pargs, _reps=1000, **kargs):
    repslist = list(range(_reps))

    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(func, *pargs, _reps=1000, **kargs):
    repslist = list(range(_reps))

    best = 2 ** 32
    for i in repslist:
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)


def bestoftotal(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
