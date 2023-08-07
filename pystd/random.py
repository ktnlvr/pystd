from typing import Sequence
import time
_seed = 4


def seed(a=None, version: int = 2):
    global _seed
    if a is None:
        _seed = int(time.time())
    _seed = a


def getstate() -> object:
    global _seed
    return _seed


def setstate(state: object):
    global _seed
    _seed = int(state)


def getrandbits(k) -> int:
    return randint(0, 2**k - 1)


def randbytes(n: int) -> bytes:
    return bytes(map(lambda _: randint(0, 255), range(n)))


def random() -> float:
    return randint(0, 10**8 - 1) / 10**8


def uniform(a: float, b: float) -> float:
    if a > b:
        a, b = b, a
    return a + (b - a) * random()


def randint(a: int, b: int) -> int:
    assert a <= b
    global _seed
    _seed = (69069 * _seed + 1) % 2**32
    return _seed % (b + 1 - a) + a


def choice(seq: Sequence) -> object:
    if not seq:
        raise IndexError
    return seq[randint(0, len(seq) - 1)]


def choices(population, weights=None, *, cumulative_weights=None, k=1) -> list:
    ls = list()
    for i in range(len(population)):
        ls = ls + [population[i]] * weights[i]
    res = list()
    for i in range(k):
        res.append(choice(ls))
    return res


def sample(population, k, *, counts=None):
    population = list(population)
    if counts is None:
        p1 = population.copy()
    else:
        p1 = list()
        for i in range(len(population)):
            p1.extend([population[i]] * counts[i])
    
    if k > len(p1):
        raise ValueError
    
    ls = list()
    for i in range(k):
        b = choice(p1)
        ls.append(b)
        p1.remove(b)
    return ls
