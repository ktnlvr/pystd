_seed = 0


def seed(a: int, version: int = 2):
    global _seed
    _seed = a


def getstate() -> object:
    ...


def setstate(state: object):
    ...


def randbytes(n: int) -> bytes:
    ...


def getrandbits(k) -> int:
    ...


def random() -> float:
    ...


def randint(a: int, b: int) -> int:
    assert a <= b
    global _seed
    _seed = (69069 * _seed + 1) % 2**32
    return _seed % (b + 1 - a) + a
