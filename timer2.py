# File timer2.py (2.x and 3.x)
"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times span(1, 2, a=3, b=4)
_reps times, and return total time for all runs, and final result.

bestof(spam, 1, 2, a=3, b=4, _reps=1000) runs best-of-N timer to attempt to
filter out the system load variation, and return best result among _reps tests.

bestoftotal(spam, 1, 2, a=3, b=4, _reps1=5, _reps=1000) runs best-of-totals
test, which take the best among _reps1 run of (the total of _reps runs);
"""

import time
import sys

if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    repslist = list(range(_reps))

    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    repslist = list(range(_reps))

    best = 2 ** 32
    for i in repslist:
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)


def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
