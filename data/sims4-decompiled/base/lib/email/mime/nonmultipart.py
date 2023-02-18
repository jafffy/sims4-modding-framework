# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\mime\nonmultipart.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 713 bytes
__all__ = [
 'MIMENonMultipart']
from email import errors
from email.mime.base import MIMEBase

class MIMENonMultipart(MIMEBase):

    def attach(self, payload):
        raise errors.MultipartConversionError('Cannot attach additional subparts to non-multipart/*')
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/mime/nonmultipart.pyc
