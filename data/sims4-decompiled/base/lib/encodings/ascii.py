# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\encodings\ascii.py
# Compiled at: 2011-04-09 03:53:23
# Size of source mod 2**32: 1298 bytes
import codecs

class Codec(codecs.Codec):
    encode = codecs.ascii_encode
    decode = codecs.ascii_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.ascii_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return codecs.ascii_decode(input, self.errors)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


class StreamConverter(StreamWriter, StreamReader):
    encode = codecs.ascii_decode
    decode = codecs.ascii_encode


def getregentry():
    return codecs.CodecInfo(name='ascii',
      encode=(Codec.encode),
      decode=(Codec.decode),
      incrementalencoder=IncrementalEncoder,
      incrementaldecoder=IncrementalDecoder,
      streamwriter=StreamWriter,
      streamreader=StreamReader)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/encodings/ascii.pyc
