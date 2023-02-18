# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\google\protobuf\internal\message_listener.py
# Compiled at: 2011-01-24 07:39:36
# Size of source mod 2**32: 3432 bytes
__author__ = 'robinson@google.com (Will Robinson)'

class MessageListener(object):

    def Modified(self):
        raise NotImplementedError


class NullMessageListener(object):

    def Modified(self):
        pass
# okay decompiling data/sims4-not-yet-decompiled/core/google/protobuf/internal/message_listener.pyc
