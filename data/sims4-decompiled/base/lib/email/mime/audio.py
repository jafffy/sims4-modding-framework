# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\mime\audio.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 2813 bytes
__all__ = [
 'MIMEAudio']
import sndhdr
from io import BytesIO
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart
_sndhdr_MIMEmap = {
 'au': "'basic'", 
 'wav': "'x-wav'", 
 'aiff': "'x-aiff'", 
 'aifc': "'x-aiff'"}

def _whatsnd(data):
    hdr = data[:512]
    fakefile = BytesIO(hdr)
    for testfn in sndhdr.tests:
        res = testfn(hdr, fakefile)
        if res is not None:
            return _sndhdr_MIMEmap.get(res[0])


class MIMEAudio(MIMENonMultipart):

    def __init__(self, _audiodata, _subtype=None, _encoder=encoders.encode_base64, *, policy=None, **_params):
        if _subtype is None:
            _subtype = _whatsnd(_audiodata)
        if _subtype is None:
            raise TypeError('Could not find audio MIME subtype')
        (MIMENonMultipart.__init__)(self, 'audio', _subtype, policy=policy, **_params)
        self.set_payload(_audiodata)
        _encoder(self)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/mime/audio.pyc
