# coding=utf-8
"""Utility functions for oc."""

import multiprocessing as mp

from functools import partial
from itertools import chain


def search_log(log_list, search_string):
    """Search through a log list for lines containing the `search_string`.
        Returns a list of the matched lines."""
    return [log_line for log_line in log_list if search_string in log_line]


def search_mult_pod_logs(pods_logs, search_string, pool_size=4):
    """Search through the logs of multiple pods, and return the combined match
    list."""
    search_func = partial(search_log, search_string=search_string)
    with mp.Pool(pool_size) as p:
        search_results = p.map(search_func, pods_logs)
    return list(chain(search_results))
