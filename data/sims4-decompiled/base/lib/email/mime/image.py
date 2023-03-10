# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\mime\image.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 1876 bytes
__all__ = [
 'MIMEImage']
import imghdr
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart

class MIMEImage(MIMENonMultipart):

    def __init__(self, _imagedata, _subtype=None, _encoder=encoders.encode_base64, *, policy=None, **_params):
        if _subtype is None:
            _subtype = imghdr.what(None, _imagedata)
        if _subtype is None:
            raise TypeError('Could not guess image MIME subtype')
        (MIMENonMultipart.__init__)(self, 'image', _subtype, policy=policy, **_params)
        self.set_payload(_imagedata)
        _encoder(self)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/mime/image.pyc
