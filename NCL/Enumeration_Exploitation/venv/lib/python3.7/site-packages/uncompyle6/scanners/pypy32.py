#  Copyright (c) 2017 by Rocky Bernstein
"""
Python PyPy 3.2 decompiler scanner.

Does some additional massaging of xdis-disassembled instructions to
make things easier for decompilation.
"""

import uncompyle6.scanners.scanner32 as scan

# bytecode verification, verify(), uses JUMP_OPs from here
from xdis.opcodes import opcode_32 as opc  # is this right?
JUMP_OPs = map(lambda op: opc.opname[op], opc.hasjrel + opc.hasjabs)

# We base this off of 3.2
class ScannerPyPy32(scan.Scanner32):
    def __init__(self, show_asm):
        # There are no differences in initialization between
        # pypy 3.2 and 3.2
        scan.Scanner32.__init__(self, show_asm, is_pypy=True)
        self.version = 3.2
        return
