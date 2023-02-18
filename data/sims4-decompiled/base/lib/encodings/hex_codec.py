# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\encodings\hex_codec.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 1563 bytes
import codecs, binascii

def hex_encode(input, errors='strict'):
    return (
     binascii.b2a_hex(input), len(input))


def hex_decode(input, errors='strict'):
    return (
     binascii.a2b_hex(input), len(input))


class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return hex_encode(input, errors)

    def decode(self, input, errors='strict'):
        return hex_decode(input, errors)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return binascii.b2a_hex(input)


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return binascii.a2b_hex(input)


class StreamWriter(Codec, codecs.StreamWriter):
    charbuffertype = bytes


class StreamReader(Codec, codecs.StreamReader):
    charbuffertype = bytes


def getregentry():
    return codecs.CodecInfo(name='hex',
      encode=hex_encode,
      decode=hex_decode,
      incrementalencoder=IncrementalEncoder,
      incrementaldecoder=IncrementalDecoder,
      streamwriter=StreamWriter,
      streamreader=StreamReader,
      _is_text_encoding=False)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/encodings/hex_codec.pyc
