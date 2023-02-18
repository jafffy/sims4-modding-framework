# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\unittest\test\testmock\__init__.py
# Compiled at: 2013-04-05 23:16:42
# Size of source mod 2**32: 482 bytes
import os, sys, unittest
here = os.path.dirname(__file__)
loader = unittest.defaultTestLoader

def load_tests(*args):
    suite = unittest.TestSuite()
    for fn in os.listdir(here):
        if fn.startswith('test') and fn.endswith('.py'):
            modname = 'unittest.test.testmock.' + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTest(loader.loadTestsFromModule(module))

    return suite
# okay decompiling data/sims4-not-yet-decompiled/base/lib/unittest/test/testmock/__init__.pyc
