import numpy as np
import torch
import tensorflow as tf
import typing


def binary_search_recursive(
    _list: typing.Iterable,
    _e: object,
    _low: int = 0,
    _high: int = None,
) -> typing.Union[int, None]:
    if _high is None:
        _high = len(_list) - 1

    if _high < _low:
        return None

    mid = _low + (_high - _low) // 2

    if _list[mid] == _e:
        return mid

    elif _list[mid] > _e:
        # _e is less than _list[mid], so solution lies on left of mid
        return binary_search_recursive(_list, _e, _low, mid - 1)

    else:
        return binary_search_recursive(_list, _e, mid + 1, _high)


def binary_search_iterative(
    _list: typing.Iterable,
    _e: typing.Any,
) -> typing.Union[int, None]:
    _low = 0
    _high = len(_list) - 1

    while _low <= _high:
        mid = _low + (_high - _low) // 2

        if _list[mid] == _e:
            return mid

        elif _list[mid] > _e:
            _high = mid - 1

        else:
            _low = mid + 1

    return None


def test_binary_search__():
    _list = list(range(100)) + [80]
    _e1 = 80
    _e2 = 5000

    print("list ==============")
    print(
        binary_search_recursive(_list, _e1),
        binary_search_iterative(_list, _e1),
    )
    print(
        binary_search_recursive(_list, _e2),
        binary_search_iterative(_list, _e2),
    )

    print("np ==============")
    _np_array = np.array(_list)
    print(
        binary_search_recursive(_np_array, _e1),
        binary_search_iterative(_np_array, _e1),
    )
    print(
        binary_search_recursive(_np_array, _e2),
        binary_search_iterative(_np_array, _e2),
    )

    print("torch ==============")
    _torch_tensor = torch.tensor(_list)
    print(
        binary_search_recursive(_torch_tensor, _e1),
        binary_search_iterative(_torch_tensor, _e1),
    )
    print(
        binary_search_recursive(_torch_tensor, _e2),
        binary_search_iterative(_torch_tensor, _e2),
    )

    print("tf ==============")
    _tf_tensor = tf.convert_to_tensor(_list)
    print(
        binary_search_recursive(_tf_tensor, _e1),
        binary_search_iterative(_tf_tensor, _e1),
    )
    print(
        binary_search_recursive(_tf_tensor, _e2),
        binary_search_iterative(_tf_tensor, _e2),
    )


if __name__ == "__main__":
    test_binary_search__()
