from pystd import random


def test_same_seed_same_random():
    random.seed(4)
    a = random.random()
    assert type(a) is float
    random.seed(4)
    b = random.random()
    assert type(b) is float
    assert a == b


def test_state_setter():
    state = random.randint(0, 100)
    random.setstate(state)
    assert random.getstate() == state


def test_randbits_len():
    random.seed(10)

    for i in range(10000):
        bits = random.getrandbits(i)
        assert type(bits) is int
        assert bits >= 0
        assert bits.bit_length() <= i


def test_randint():
    random.seed(10)

    for i in range(10000):
        a = random.randint(0, i)
        b = random.randint(a+1, (i+1)**2)
        n = random.randint(a, b)
        assert a <= n <= b
