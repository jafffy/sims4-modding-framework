# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\xml\dom\NodeFilter.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 963 bytes


class NodeFilter:
    FILTER_ACCEPT = 1
    FILTER_REJECT = 2
    FILTER_SKIP = 3
    SHOW_ALL = 4294967295
    SHOW_ELEMENT = 1
    SHOW_ATTRIBUTE = 2
    SHOW_TEXT = 4
    SHOW_CDATA_SECTION = 8
    SHOW_ENTITY_REFERENCE = 16
    SHOW_ENTITY = 32
    SHOW_PROCESSING_INSTRUCTION = 64
    SHOW_COMMENT = 128
    SHOW_DOCUMENT = 256
    SHOW_DOCUMENT_TYPE = 512
    SHOW_DOCUMENT_FRAGMENT = 1024
    SHOW_NOTATION = 2048

    def acceptNode(self, node):
        raise NotImplementedError
# okay decompiling data/sims4-not-yet-decompiled/base/lib/xml/dom/NodeFilter.pyc
