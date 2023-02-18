# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Dec  7 2022, 01:12:33) 
# [GCC 11.3.0]
# Embedded file name: T:\InGame\Gameplay\Scripts\Lib\email\errors.py
# Compiled at: 2013-04-05 23:16:39
# Size of source mod 2**32: 3642 bytes


class MessageError(Exception):
    pass


class MessageParseError(MessageError):
    pass


class HeaderParseError(MessageParseError):
    pass


class BoundaryError(MessageParseError):
    pass


class MultipartConversionError(MessageError, TypeError):
    pass


class CharsetError(MessageError):
    pass


class MessageDefect(ValueError):

    def __init__(self, line=None):
        if line is not None:
            super().__init__(line)
        self.line = line


class NoBoundaryInMultipartDefect(MessageDefect):
    pass


class StartBoundaryNotFoundDefect(MessageDefect):
    pass


class CloseBoundaryNotFoundDefect(MessageDefect):
    pass


class FirstHeaderLineIsContinuationDefect(MessageDefect):
    pass


class MisplacedEnvelopeHeaderDefect(MessageDefect):
    pass


class MissingHeaderBodySeparatorDefect(MessageDefect):
    pass


MalformedHeaderDefect = MissingHeaderBodySeparatorDefect

class MultipartInvariantViolationDefect(MessageDefect):
    pass


class InvalidMultipartContentTransferEncodingDefect(MessageDefect):
    pass


class UndecodableBytesDefect(MessageDefect):
    pass


class InvalidBase64PaddingDefect(MessageDefect):
    pass


class InvalidBase64CharactersDefect(MessageDefect):
    pass


class HeaderDefect(MessageDefect):

    def __init__(self, *args, **kw):
        (super().__init__)(*args, **kw)


class InvalidHeaderDefect(HeaderDefect):
    pass


class HeaderMissingRequiredValue(HeaderDefect):
    pass


class NonPrintableDefect(HeaderDefect):

    def __init__(self, non_printables):
        super().__init__(non_printables)
        self.non_printables = non_printables

    def __str__(self):
        return 'the following ASCII non-printables found in header: {}'.format(self.non_printables)


class ObsoleteHeaderDefect(HeaderDefect):
    pass


class NonASCIILocalPartDefect(HeaderDefect):
    pass
# okay decompiling data/sims4-not-yet-decompiled/base/lib/email/errors.pyc
