from typing import Sequence

_seed = 0


def seed(a: int = None, version: int = 2):
    global _seed
    _seed = a


def getstate() -> object:
    ...


def setstate(state: object):
    ...


def getrandbits(k) -> int:
    ...


def randbytes(n: int) -> bytes:
    ...


def random() -> float:
    ...


def uniform(a: float, b: float) -> float:
    ...


def randint(a: int, b: int) -> int:
    assert a <= b
    global _seed
    _seed = (69069 * _seed + 1) % 2**32
    return _seed % (b + 1 - a) + a


def choice(seq: Sequence) -> object:
    ...


def choices(
    population, weights=None, *, cumulative_weights=None, k=1
) -> list:
    ...


def shuffle(seq: Sequence) -> object:
    ...


def sample(population, k, *, counts=None):
    ...
