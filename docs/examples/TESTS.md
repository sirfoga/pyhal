# hal.tests

## battery_test()
```python
from unittest import TestCase

from hal.maths.maths import Integer
from hal.tests.utils import battery_test, random_name


def is_prime(string):
    return Integer(string).is_probably_prime()

class EasyTest(TestCase):
    def test_primality(self):
        tests = {
            "2": True,  # 2 is prime
            "3": True,  # 3 is also prime
            "4": False,  # 4 is NOT a prime (2 * 2)
            "997": True,  # should be prime
            "4366114": False,  # not a prime (divisible by 2)
            "14553714337": True,  # this should be prime
            "58853781722270786163": False  # not a prime (divisible by 3)
        }

        battery_test(
            self.assertEquals, tests, is_prime
        )
```

```bash
Ran 1 test in 0.000s

OK
```


## Questions and issues
The [github issue tracker](https://github.com/sirfoga/pyhal/issues) is **only** for bug reports and feature requests. Anything else, such as questions for help in using the library, should be mailed [here](mailto:sirfoga@protonmail.com).
