import numpy as np
import torch
import tensorflow as tf
import typing


def linear_search(
    _list: typing.Union[
        typing.List,
        np.ndarray,
        torch.Tensor,
        tf.Tensor,
    ],
    _e: typing.Any,
):
    if isinstance(_list, list):
        try:
            return _list.index(_e)
        except ValueError:
            return None

    elif isinstance(_list, tuple):
        return linear_search(list(_list), _e)

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


def linear_search_scratch(_list, _e):
    for i in range(len(_list)):
        if _list[i] == _e:
            return i

    return None


def test_linear_search__():
    _list = list(range(100)) + [80]
    _e1 = 80
    _e2 = 5000

    print("list ==============")
    print(linear_search(_list, _e1), linear_search_scratch(_list, _e1))
    print(linear_search(_list, _e2), linear_search_scratch(_list, _e2))

    print("np ==============")
    _np_array = np.array(_list)
    print(linear_search(_np_array, _e1), linear_search_scratch(_np_array, _e1))
    print(linear_search(_np_array, _e2), linear_search_scratch(_np_array, _e2))

    print("torch ==============")
    _torch_tensor = torch.tensor(_list)
    print(linear_search(_torch_tensor, _e1), linear_search_scratch(_torch_tensor, _e1))
    print(linear_search(_torch_tensor, _e2), linear_search_scratch(_torch_tensor, _e2))

    print("tf ==============")
    _tf_tensor = tf.convert_to_tensor(_list)
    print(linear_search(_tf_tensor, _e1), linear_search_scratch(_tf_tensor, _e1))
    print(linear_search(_tf_tensor, _e2), linear_search_scratch(_tf_tensor, _e2))


if __name__ == "__main__":
    test_linear_search__()
