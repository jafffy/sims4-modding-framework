# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\sunau.py
# Compiled at: 2018-06-27 03:07:36
# Size of source mod 2**32: 18906 bytes
from collections import namedtuple
import warnings
_sunau_params = namedtuple('_sunau_params', 'nchannels sampwidth framerate nframes comptype compname')
AUDIO_FILE_MAGIC = 779316836
AUDIO_FILE_ENCODING_MULAW_8 = 1
AUDIO_FILE_ENCODING_LINEAR_8 = 2
AUDIO_FILE_ENCODING_LINEAR_16 = 3
AUDIO_FILE_ENCODING_LINEAR_24 = 4
AUDIO_FILE_ENCODING_LINEAR_32 = 5
AUDIO_FILE_ENCODING_FLOAT = 6
AUDIO_FILE_ENCODING_DOUBLE = 7
AUDIO_FILE_ENCODING_ADPCM_G721 = 23
AUDIO_FILE_ENCODING_ADPCM_G722 = 24
AUDIO_FILE_ENCODING_ADPCM_G723_3 = 25
AUDIO_FILE_ENCODING_ADPCM_G723_5 = 26
AUDIO_FILE_ENCODING_ALAW_8 = 27
AUDIO_UNKNOWN_SIZE = 4294967295
_simple_encodings = [
 'AUDIO_FILE_ENCODING_MULAW_8', 
 'AUDIO_FILE_ENCODING_LINEAR_8', 
 'AUDIO_FILE_ENCODING_LINEAR_16', 
 'AUDIO_FILE_ENCODING_LINEAR_24', 
 'AUDIO_FILE_ENCODING_LINEAR_32', 
 'AUDIO_FILE_ENCODING_ALAW_8']

class Error(Exception):
    pass


def _read_u32(file):
    x = 0
    for i in range(4):
        byte = file.read(1)
        if not byte:
            raise EOFError
        x = x * 256 + ord(byte)

    return x


def _write_u32(file, x):
    data = []
    for i in range(4):
        d, m = divmod(x, 256)
        data.insert(0, int(m))
        x = d

    file.write(bytes(data))


class Au_read:

    def __init__(self, f):
        if type(f) == type(''):
            import builtins
            f = builtins.open(f, 'rb')
            self._opened = True
        else:
            self._opened = False
        self.initfp(f)

    def __del__(self):
        if self._file:
            self.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def initfp(self, file):
        self._file = file
        self._soundpos = 0
        magic = int(_read_u32(file))
        if magic != AUDIO_FILE_MAGIC:
            raise Error('bad magic number')
        self._hdr_size = int(_read_u32(file))
        if self._hdr_size < 24:
            raise Error('header size too small')
        if self._hdr_size > 100:
            raise Error('header size ridiculously large')
        self._data_size = _read_u32(file)
        if self._data_size != AUDIO_UNKNOWN_SIZE:
            self._data_size = int(self._data_size)
        self._encoding = int(_read_u32(file))
        if self._encoding not in _simple_encodings:
            raise Error('encoding not (yet) supported')
        else:
            if self._encoding in (AUDIO_FILE_ENCODING_MULAW_8,
             AUDIO_FILE_ENCODING_ALAW_8):
                self._sampwidth = 2
                self._framesize = 1
            else:
                if self._encoding == AUDIO_FILE_ENCODING_LINEAR_8:
                    self._framesize = self._sampwidth = 1
                else:
                    if self._encoding == AUDIO_FILE_ENCODING_LINEAR_16:
                        self._framesize = self._sampwidth = 2
                    else:
                        if self._encoding == AUDIO_FILE_ENCODING_LINEAR_24:
                            self._framesize = self._sampwidth = 3
                        else:
                            if self._encoding == AUDIO_FILE_ENCODING_LINEAR_32:
                                self._framesize = self._sampwidth = 4
                            else:
                                raise Error('unknown encoding')
            self._framerate = int(_read_u32(file))
            self._nchannels = int(_read_u32(file))
            if not self._nchannels:
                raise Error('bad # of channels')
            self._framesize = self._framesize * self._nchannels
            if self._hdr_size > 24:
                self._info = file.read(self._hdr_size - 24)
                self._info, _, _ = self._info.partition(b'\x00')
            else:
                self._info = b''
        try:
            self._data_pos = file.tell()
        except (AttributeError, OSError):
            self._data_pos = None

    def getfp(self):
        return self._file

    def getnchannels(self):
        return self._nchannels

    def getsampwidth(self):
        return self._sampwidth

    def getframerate(self):
        return self._framerate

    def getnframes(self):
        if self._data_size == AUDIO_UNKNOWN_SIZE:
            return AUDIO_UNKNOWN_SIZE
        if self._encoding in _simple_encodings:
            return self._data_size // self._framesize
        return 0

    def getcomptype(self):
        if self._encoding == AUDIO_FILE_ENCODING_MULAW_8:
            return 'ULAW'
        if self._encoding == AUDIO_FILE_ENCODING_ALAW_8:
            return 'ALAW'
        return 'NONE'

    def getcompname(self):
        if self._encoding == AUDIO_FILE_ENCODING_MULAW_8:
            return 'CCITT G.711 u-law'
        if self._encoding == AUDIO_FILE_ENCODING_ALAW_8:
            return 'CCITT G.711 A-law'
        return 'not compressed'

    def getparams(self):
        return _sunau_params(self.getnchannels(), self.getsampwidth(), self.getframerate(), self.getnframes(), self.getcomptype(), self.getcompname())

    def getmarkers(self):
        pass

    def getmark(self, id):
        raise Error('no marks')

    def readframes(self, nframes):
        if self._encoding in _simple_encodings:
            if nframes == AUDIO_UNKNOWN_SIZE:
                data = self._file.read()
            else:
                data = self._file.read(nframes * self._framesize)
            self._soundpos += len(data) // self._framesize
            if self._encoding == AUDIO_FILE_ENCODING_MULAW_8:
                import audioop
                data = audioop.ulaw2lin(data, self._sampwidth)
            return data

    def rewind(self):
        if self._data_pos is None:
            raise OSError('cannot seek')
        self._file.seek(self._data_pos)
        self._soundpos = 0

    def tell(self):
        return self._soundpos

    def setpos(self, pos):
        if pos < 0 or pos > self.getnframes():
            raise Error('position not in range')
        if self._data_pos is None:
            raise OSError('cannot seek')
        self._file.seek(self._data_pos + pos * self._framesize)
        self._soundpos = pos

    def close(self):
        file = self._file
        if file:
            self._file = None
            if self._opened:
                file.close()


class Au_write:

    def __init__(self, f):
        if type(f) == type(''):
            import builtins
            f = builtins.open(f, 'wb')
            self._opened = True
        else:
            self._opened = False
        self.initfp(f)

    def __del__(self):
        if self._file:
            self.close()
        self._file = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def initfp(self, file):
        self._file = file
        self._framerate = 0
        self._nchannels = 0
        self._sampwidth = 0
        self._framesize = 0
        self._nframes = AUDIO_UNKNOWN_SIZE
        self._nframeswritten = 0
        self._datawritten = 0
        self._datalength = 0
        self._info = b''
        self._comptype = 'ULAW'

    def setnchannels(self, nchannels):
        if self._nframeswritten:
            raise Error('cannot change parameters after starting to write')
        if nchannels not in (1, 2, 4):
            raise Error('only 1, 2, or 4 channels supported')
        self._nchannels = nchannels

    def getnchannels(self):
        if not self._nchannels:
            raise Error('number of channels not set')
        return self._nchannels

    def setsampwidth(self, sampwidth):
        if self._nframeswritten:
            raise Error('cannot change parameters after starting to write')
        if sampwidth not in (1, 2, 3, 4):
            raise Error('bad sample width')
        self._sampwidth = sampwidth

    def getsampwidth(self):
        if not self._framerate:
            raise Error('sample width not specified')
        return self._sampwidth

    def setframerate(self, framerate):
        if self._nframeswritten:
            raise Error('cannot change parameters after starting to write')
        self._framerate = framerate

    def getframerate(self):
        if not self._framerate:
            raise Error('frame rate not set')
        return self._framerate

    def setnframes(self, nframes):
        if self._nframeswritten:
            raise Error('cannot change parameters after starting to write')
        if nframes < 0:
            raise Error('# of frames cannot be negative')
        self._nframes = nframes

    def getnframes(self):
        return self._nframeswritten

    def setcomptype(self, type, name):
        if type in ('NONE', 'ULAW'):
            self._comptype = type
        else:
            raise Error('unknown compression type')

    def getcomptype(self):
        return self._comptype

    def getcompname(self):
        if self._comptype == 'ULAW':
            return 'CCITT G.711 u-law'
        if self._comptype == 'ALAW':
            return 'CCITT G.711 A-law'
        return 'not compressed'

    def setparams(self, params):
        nchannels, sampwidth, framerate, nframes, comptype, compname = params
        self.setnchannels(nchannels)
        self.setsampwidth(sampwidth)
        self.setframerate(framerate)
        self.setnframes(nframes)
        self.setcomptype(comptype, compname)

    def getparams(self):
        return _sunau_params(self.getnchannels(), self.getsampwidth(), self.getframerate(), self.getnframes(), self.getcomptype(), self.getcompname())

    def tell(self):
        return self._nframeswritten

    def writeframesraw(self, data):
        if not isinstance(data, (bytes, bytearray)):
            data = memoryview(data).cast('B')
        self._ensure_header_written()
        if self._comptype == 'ULAW':
            import audioop
            data = audioop.lin2ulaw(data, self._sampwidth)
        nframes = len(data) // self._framesize
        self._file.write(data)
        self._nframeswritten = self._nframeswritten + nframes
        self._datawritten = self._datawritten + len(data)

    def writeframes(self, data):
        self.writeframesraw(data)
        if self._nframeswritten != self._nframes or self._datalength != self._datawritten:
            self._patchheader()

    def close(self):
        if self._file:
            try:
                self._ensure_header_written()
                if self._nframeswritten != self._nframes or self._datalength != self._datawritten:
                    self._patchheader()
                self._file.flush()
            finally:
                file = self._file
                self._file = None
                if self._opened:
                    file.close()

    def _ensure_header_written(self):
        if not self._nframeswritten:
            if not self._nchannels:
                raise Error('# of channels not specified')
            else:
                if not self._sampwidth:
                    raise Error('sample width not specified')
                assert self._framerate, 'frame rate not specified'
            self._write_header()

    def _write_header(self):
        if self._comptype == 'NONE':
            if self._sampwidth == 1:
                encoding = AUDIO_FILE_ENCODING_LINEAR_8
                self._framesize = 1
            elif self._sampwidth == 2:
                encoding = AUDIO_FILE_ENCODING_LINEAR_16
                self._framesize = 2
            elif self._sampwidth == 3:
                encoding = AUDIO_FILE_ENCODING_LINEAR_24
                self._framesize = 3
            elif self._sampwidth == 4:
                encoding = AUDIO_FILE_ENCODING_LINEAR_32
                self._framesize = 4
            else:
                raise Error('internal error')
        elif self._comptype == 'ULAW':
            encoding = AUDIO_FILE_ENCODING_MULAW_8
            self._framesize = 1
        else:
            raise Error('internal error')
        self._framesize = self._framesize * self._nchannels
        _write_u32(self._file, AUDIO_FILE_MAGIC)
        header_size = 25 + len(self._info)
        header_size = header_size + 7 & -8
        _write_u32(self._file, header_size)
        if self._nframes == AUDIO_UNKNOWN_SIZE:
            length = AUDIO_UNKNOWN_SIZE
        else:
            length = self._nframes * self._framesize
        try:
            self._form_length_pos = self._file.tell()
        except (AttributeError, OSError):
            self._form_length_pos = None

        _write_u32(self._file, length)
        self._datalength = length
        _write_u32(self._file, encoding)
        _write_u32(self._file, self._framerate)
        _write_u32(self._file, self._nchannels)
        self._file.write(self._info)
        self._file.write(b'\x00' * (header_size - len(self._info) - 24))

    def _patchheader(self):
        if self._form_length_pos is None:
            raise OSError('cannot seek')
        self._file.seek(self._form_length_pos)
        _write_u32(self._file, self._datawritten)
        self._datalength = self._datawritten
        self._file.seek(0, 2)


def open(f, mode=None):
    if mode is None:
        if hasattr(f, 'mode'):
            mode = f.mode
        else:
            mode = 'rb'
    if mode in ('r', 'rb'):
        return Au_read(f)
    if mode in ('w', 'wb'):
        return Au_write(f)
    raise Error("mode must be 'r', 'rb', 'w', or 'wb'")


def openfp(f, mode=None):
    warnings.warn('sunau.openfp is deprecated since Python 3.7. Use sunau.open instead.', DeprecationWarning,
      stacklevel=2)
    return open(f, mode=mode)
# okay decompiling data/sims4-not-yet-decompiled/base/lib/sunau.pyc
