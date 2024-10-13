import numpy as np
import torch
import tensorflow as tf
import typing


def ternary_search_recursive(
    _list: typing.Iterable,
    _e: object,
    _low: int = 0,
    _high: int = None,
) -> typing.Union[int, None]:
    if _high is None:
        _high = len(_list) - 1

    if _high < _low:
        return None

    mid1 = _low + (_high - _low) // 3
    mid2 = _high - (_high - _low) // 3

    if _list[mid1] == _e:
        return mid1

    if _list[mid2] == _e:
        return mid2

    if _e < _list[mid1]:
        return ternary_search_recursive(_list, _e, _low, mid1 - 1)
    elif _e > _list[mid2]:
        return ternary_search_recursive(_list, _e, mid2 + 1, _high)
    else:
        return ternary_search_recursive(_list, _e, mid1 + 1, mid2 - 1)


def ternary_search_iterative(
    _list: typing.Iterable,
    _e: typing.Any,
) -> typing.Union[int, None]:
    _low = 0
    _high = len(_list) - 1

    while _low <= _high:
        mid1 = _low + (_high - _low) // 3
        mid2 = _high - (_high - _low) // 3

        if _list[mid1] == _e:
            return mid1

        if _list[mid2] == _e:
            return mid2

        if _e < _list[mid1]:
            _high = mid1 - 1
        elif _e > _list[mid2]:
            _low = mid2 + 1
        else:
            _low, _high = mid1 + 1, mid2 - 1

    return None


def test_ternary_search__():
    _list = list(range(100))
    _e1 = 80
    _e2 = 5000

    print("list ==============")
    print(
        ternary_search_recursive(_list, _e1),
        ternary_search_iterative(_list, _e1),
    )
    print(
        ternary_search_recursive(_list, _e2),
        ternary_search_iterative(_list, _e2),
    )

    print("np ==============")
    _np_array = np.array(_list)
    print(
        ternary_search_recursive(_np_array, _e1),
        ternary_search_iterative(_np_array, _e1),
    )
    print(
        ternary_search_recursive(_np_array, _e2),
        ternary_search_iterative(_np_array, _e2),
    )

    print("torch ==============")
    _torch_tensor = torch.tensor(_list)
    print(
        ternary_search_recursive(_torch_tensor, _e1),
        ternary_search_iterative(_torch_tensor, _e1),
    )
    print(
        ternary_search_recursive(_torch_tensor, _e2),
        ternary_search_iterative(_torch_tensor, _e2),
    )

    print("tf ==============")
    _tf_tensor = tf.convert_to_tensor(_list)
    print(
        ternary_search_recursive(_tf_tensor, _e1),
        ternary_search_iterative(_tf_tensor, _e1),
    )
    print(
        ternary_search_recursive(_tf_tensor, _e2),
        ternary_search_iterative(_tf_tensor, _e2),
    )


if __name__ == "__main__":
    test_ternary_search__()
