import math
from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    if parity == Parity.ODD:
        return [i for i in range(start, stop) if i % 2 != 0]
    else:
        return [i for i in range(start, stop) if i % 2 == 0]
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    result = {}
    for i in range(start, stop):
        result[i] = strategy(i)
    return result
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """



def gen_set(val_in: str) -> Set:
    return set([i.upper() for i in val_in if i != i.upper()])

    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """

