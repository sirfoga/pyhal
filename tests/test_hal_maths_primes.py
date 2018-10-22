# -*- coding: utf-8 -*-


"""Tests hal.maths.primes implementation"""

from scipy.stats import describe

from hal.maths.primes import get_prime, Integer, blum_blum_shub


def test_get_prime():
    """Tests hal.maths.primes.get_prime method"""

    bits = range(2, 20, 2)  # different sizes
    for n_bits in bits:
        prime = get_prime(n_bits)
        assert Integer(str(prime)).is_probably_prime()

        not_prime = prime - 1  # definitely NOT a prime
        assert not Integer(str(not_prime)).is_probably_prime()


def test_blum_blum_shub():
    """Tests hal.maths.primes.blum_blum_shub method"""

    seed = 6
    amount = 40
    primes = (83, 103)  # must be == 3 mod 4
    randoms = blum_blum_shub(seed, amount, primes[0], primes[1])

    assert len(randoms) == amount

    distribution = describe(randoms)

    assert abs(distribution.skewness) <= 0.5

    assert not blum_blum_shub(seed, 0, primes[0], primes[1])


class TestInteger:
    """Tests Integer class"""

    @staticmethod
    def test_is_naive_prime():
        """Tests hal.maths.primes.Integer.is_naive_prime method"""

        assert not Integer("1").is_naive_prime()

    @staticmethod
    def test_is_probably_prime():
        """Tests hal.maths.primes.Integer.is_probably_prime method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_test_miller_rabin():
        """Tests hal.maths.primes.Integer.test_miller_rabin method"""

        pass  # todo auto generated method stub
