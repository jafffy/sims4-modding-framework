# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\mime\multipart.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 1669 bytes
__all__ = [
 'MIMEMultipart']
from email.mime.base import MIMEBase

class MIMEMultipart(MIMEBase):

    def __init__(self, _subtype='mixed', boundary=None, _subparts=None, *, policy=None, **_params):
        (MIMEBase.__init__)(self, 'multipart', _subtype, policy=policy, **_params)
        self._payload = []
        if _subparts:
            for p in _subparts:
                self.attach(p)

        if boundary:
            self.set_boundary(boundary)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/mime/multipart.pyc
