import numpy as np

from locust.geometry.extract_network import find_paths, is_new_path, Path


def test_is_new_path():
    p123 = Path(start=(1, 1), stop=(3, 1), path=[(1, 1), (2, 1), (3, 1)])
    assert is_new_path([], p123)
    assert not is_new_path(
        [p123], Path(start=(1, 1), stop=(3, 1), path=[(1, 1), (2, 1), (2, 2), (3, 2), (3, 1)])
    )


def test_find_paths():
    skel = np.array([[0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0],])
    nodes = [(1, 1), (3, 1), (1, 3)]
    paths = find_paths(skel, nodes)
    assert paths == [
        Path(start=(1, 1), stop=(3, 1), path=[(1, 1), (2, 1), (3, 1)]),
        Path(start=(1, 1), stop=(1, 3), path=[(1, 1), (1, 2), (1, 3)]),
    ]


def test_find_paths_self_loop():
    skel = np.array([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0],])
    nodes = [(1, 1)]
    paths = find_paths(skel, nodes)
    assert paths == [
        Path(start=(1, 1), stop=(1, 1), path=[(1, 1), (1, 2), (2, 3), (3, 2), (2, 1), (1, 1)]),
    ]
