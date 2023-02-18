# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\mime\base.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 946 bytes
__all__ = [
 'MIMEBase']
import email.policy
from email import message

class MIMEBase(message.Message):

    def __init__(self, _maintype, _subtype, *, policy=None, **_params):
        if policy is None:
            policy = email.policy.compat32
        message.Message.__init__(self, policy=policy)
        ctype = '%s/%s' % (_maintype, _subtype)
        (self.add_header)('Content-Type', ctype, **_params)
        self['MIME-Version'] = '1.0'
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/mime/base.pyc
