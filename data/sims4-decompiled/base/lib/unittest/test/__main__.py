# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\unittest\test\__main__.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 614 bytes
import os, unittest

def load_tests(loader, standard_tests, pattern):
    this_dir = os.path.dirname(__file__)
    pattern = pattern or 'test_*.py'
    top_level_dir = os.path.dirname(os.path.dirname(this_dir))
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern, top_level_dir=top_level_dir)
    standard_tests.addTests(package_tests)
    return standard_tests


if __name__ == '__main__':
    unittest.main()
# okay decompiling data/sims4-not-yet-decompiled/base/lib/unittest/test/__main__.pyc
