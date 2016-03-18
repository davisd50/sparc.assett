import unittest
from sparc.testing.fixture import test_suite_mixin


class test_suite(test_suite_mixin):
    package = 'sparc.asset.location'
    module = 'location'


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')