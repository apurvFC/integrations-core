# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
"""
Generic (typed) utilities.

NOTE: these can't live under `datadog_checks.base.utils.common` (yet) as there are some
subtleties with getting `mypy` to work with namespace packages.
See: https://github.com/python/mypy/issues/5759
"""

import itertools
from typing import Callable, Iterator, Sequence, Tuple, TypeVar

from six.moves import filterfalse

T = TypeVar("T")


def partition(
    pred,  # type: Callable[[T], bool]
    seq,  # type: Sequence[T]
):
    # type: (...) -> Tuple[Tuple[T, ...], Tuple[T, ...]]
    """
    Use a predicate to partition entries into true entries and false entries.

    Adapted from itertools recipes:
    https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    t1, t2 = itertools.tee(seq)
    return tuple(filter(pred, t1)), tuple(filterfalse(pred, t2))


def batches(seq, size):
    # type: (Sequence[T], int) -> Iterator[Sequence[T]]
    """
    Slice a sequence into batches of equal `size` (except maybe for the last batch).
    """
    for start in range(0, len(seq), size):
        end = start + size
        yield seq[start:end]
