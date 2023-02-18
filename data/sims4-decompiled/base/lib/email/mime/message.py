# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\mime\message.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 1351 bytes
__all__ = [
 'MIMEMessage']
from email import message
from email.mime.nonmultipart import MIMENonMultipart

class MIMEMessage(MIMENonMultipart):

    def __init__(self, _msg, _subtype='rfc822', *, policy=None):
        MIMENonMultipart.__init__(self, 'message', _subtype, policy=policy)
        if not isinstance(_msg, message.Message):
            raise TypeError('Argument is not an instance of Message')
        message.Message.attach(self, _msg)
        self.set_default_type('message/rfc822')
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/mime/message.pyc
