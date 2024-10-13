import numpy as np
import torch
import tensorflow as tf
import typing

from binary import binary_search_recursive


def exponential_search(
    _list: typing.Iterable,
    _e: typing.Any,
) -> typing.Union[int, None]:
    if _list[0] == _e:
        return 0

    i = 1
    n = len(_list)
    while i < n and _list[i] <= _e:
        i = i * 2

    return binary_search_recursive(_list, _e, i // 2, min(i, n - 1))
