# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\mime\text.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 1479 bytes
__all__ = [
 'MIMEText']
from email.charset import Charset
from email.mime.nonmultipart import MIMENonMultipart

class MIMEText(MIMENonMultipart):

    def __init__(self, _text, _subtype='plain', _charset=None, *, policy=None):
        if _charset is None:
            try:
                _text.encode('us-ascii')
                _charset = 'us-ascii'
            except UnicodeEncodeError:
                _charset = 'utf-8'

        (MIMENonMultipart.__init__)(self, 'text', _subtype, policy=policy, **{'charset': str(_charset)})
        self.set_payload(_text, _charset)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/mime/text.pyc
