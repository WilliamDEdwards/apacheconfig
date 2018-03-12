#
# This file is part of apacheconfig software.
#
# Copyright (c) 2018, Ilya Etingof <etingof@gmail.com>
# License: https://github.com/etingof/apacheconfig/LICENSE
#
try:
    import unittest2 as unittest

except ImportError:
    import unittest

suite = unittest.TestLoader().loadTestsFromNames(
    [#'tests.test_perl_nested.suite',
     'tests.unit.suite']
)


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
