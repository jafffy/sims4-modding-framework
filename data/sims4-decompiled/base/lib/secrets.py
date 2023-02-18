# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\secrets.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 2111 bytes
__all__ = [
 "'choice'", "'randbelow'", "'randbits'", "'SystemRandom'", 
 "'token_bytes'", 
 "'token_hex'", "'token_urlsafe'", 
 "'compare_digest'"]
import base64, binascii, os
from hmac import compare_digest
from random import SystemRandom
_sysrand = SystemRandom()
randbits = _sysrand.getrandbits
choice = _sysrand.choice

def randbelow(exclusive_upper_bound):
    if exclusive_upper_bound <= 0:
        raise ValueError('Upper bound must be positive.')
    return _sysrand._randbelow(exclusive_upper_bound)


DEFAULT_ENTROPY = 32

def token_bytes(nbytes=None):
    if nbytes is None:
        nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)


def token_hex(nbytes=None):
    return binascii.hexlify(token_bytes(nbytes)).decode('ascii')


def token_urlsafe(nbytes=None):
    tok = token_bytes(nbytes)
    return base64.urlsafe_b64encode(tok).rstrip(b'=').decode('ascii')
# okay decompiling data/sims4-not-yet-decompiled/base/lib/secrets.pyc
