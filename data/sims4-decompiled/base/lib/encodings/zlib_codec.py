# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\encodings\zlib_codec.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 2281 bytes
import codecs, zlib

def zlib_encode(input, errors='strict'):
    return (
     zlib.compress(input), len(input))


def zlib_decode(input, errors='strict'):
    return (
     zlib.decompress(input), len(input))


class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return zlib_encode(input, errors)

    def decode(self, input, errors='strict'):
        return zlib_decode(input, errors)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def __init__(self, errors='strict'):
        self.errors = errors
        self.compressobj = zlib.compressobj()

    def encode(self, input, final=False):
        if final:
            c = self.compressobj.compress(input)
            return c + self.compressobj.flush()
        return self.compressobj.compress(input)

    def reset(self):
        self.compressobj = zlib.compressobj()


class IncrementalDecoder(codecs.IncrementalDecoder):

    def __init__(self, errors='strict'):
        self.errors = errors
        self.decompressobj = zlib.decompressobj()

    def decode(self, input, final=False):
        if final:
            c = self.decompressobj.decompress(input)
            return c + self.decompressobj.flush()
        return self.decompressobj.decompress(input)

    def reset(self):
        self.decompressobj = zlib.decompressobj()


class StreamWriter(Codec, codecs.StreamWriter):
    charbuffertype = bytes


class StreamReader(Codec, codecs.StreamReader):
    charbuffertype = bytes


def getregentry():
    return codecs.CodecInfo(name='zlib',
      encode=zlib_encode,
      decode=zlib_decode,
      incrementalencoder=IncrementalEncoder,
      incrementaldecoder=IncrementalDecoder,
      streamreader=StreamReader,
      streamwriter=StreamWriter,
      _is_text_encoding=False)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/encodings/zlib_codec.pyc
