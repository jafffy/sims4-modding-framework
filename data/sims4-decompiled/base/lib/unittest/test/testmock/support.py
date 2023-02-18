# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\unittest\test\testmock\support.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 408 bytes


def is_instance(obj, klass):
    return issubclass(type(obj), klass)


class SomeClass(object):
    class_attribute = None

    def wibble(self):
        pass


class X(object):
    pass


def examine_warnings(func):

    def wrapper():
        with catch_warnings(record=True) as (ws):
            func(ws)

    return wrapper
# okay decompiling data/sims4-not-yet-decompiled/base/lib/unittest/test/testmock/support.pyc
