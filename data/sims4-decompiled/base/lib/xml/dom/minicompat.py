# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\xml\dom\minicompat.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 3476 bytes
__all__ = [
 'NodeList', 'EmptyNodeList', 'StringTypes', 'defproperty']
import xml.dom
StringTypes = (
 str,)

class NodeList(list):
    __slots__ = ()

    def item(self, index):
        if 0 <= index < len(self):
            return self[index]

    def _get_length(self):
        return len(self)

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc='The number of nodes in the NodeList.')

    def __setstate__(self, state):
        if state is None:
            state = []
        self[:] = state


class EmptyNodeList(tuple):
    __slots__ = ()

    def __add__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def __radd__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def item(self, index):
        pass

    def _get_length(self):
        return 0

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc='The number of nodes in the NodeList.')


def defproperty(klass, name, doc):
    get = getattr(klass, '_get_' + name)

    def set(self, value, name=name):
        raise xml.dom.NoModificationAllowedErr('attempt to modify read-only attribute ' + repr(name))

    prop = property(get, set, doc=doc)
    setattr(klass, name, prop)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/xml/dom/minicompat.pyc
