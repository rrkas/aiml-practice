import numpy as np
import torch
import tensorflow as tf
import typing


def linear_search_optimal(
    _list: typing.Union[
        typing.List,
        np.ndarray,
        torch.Tensor,
        tf.Tensor,
    ],
    _e: typing.Any,
) -> typing.Union[int, None]:
    if isinstance(_list, list):
        try:
            return _list.index(_e)
        except ValueError:
            return None

    elif isinstance(_list, tuple):
        return linear_search_optimal(list(_list), _e)

    elif isinstance(_list, np.ndarray):
        idx_list = np.where(_list == _e)[0]

        if idx_list.size > 0:
            return idx_list[0]

        return None

    elif isinstance(_list, torch.Tensor):
        idx_tensor = torch.nonzero(_list == _e, as_tuple=False)

        if idx_tensor.size(0) > 0:
            return idx_tensor[0].item()

        return None

    elif isinstance(_list, tf.Tensor):
        idx_tensor = tf.where(tf.equal(_list, _e))

        if tf.size(idx_tensor) > 0:
            return idx_tensor[0][0].numpy()

        return None

    raise Exception(f"Unhandled input list type: {type(_list)}")


def linear_search_scratch(
    _list: typing.Iterable,
    _e: typing.Any,
) -> typing.Union[int, None]:
    for i in range(len(_list)):
        if _list[i] == _e:
            return i

    return None
