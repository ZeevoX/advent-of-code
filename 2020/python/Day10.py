#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

xs = [0] + sorted(aoc_utils.input_int_list())

di = {}
for i, x in enumerate(xs):
    di[x] = [x + j for j in [1, 2, 3] if x + j in xs[i + 1 : i + 4]]

e = max(di.keys())

cache = {}


def paths(k):
    p = 0
    if k >= e:
        return 1
    for s in di[k]:
        if s not in cache:
            cache[s] = paths(s)
        p += cache[s]
    return p


print(paths(0))
