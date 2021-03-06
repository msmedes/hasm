from typing import Optional

from hasm.types import SymTable


class SymbolTable:

    __SYM: SymTable = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "r0": 0,
        "R0": 0,
        "r1": 1,
        "R1": 1,
        "r2": 2,
        "R2": 2,
        "r3": 3,
        "R3": 3,
        "r4": 4,
        "R4": 4,
        "r5": 5,
        "R5": 5,
        "r6": 6,
        "R6": 6,
        "r7": 7,
        "R7": 7,
        "r8": 8,
        "R8": 8,
        "r9": 9,
        "R9": 9,
        "r10": 10,
        "R10": 10,
        "r11": 11,
        "R11": 11,
        "r12": 12,
        "R12": 12,
        "r13": 13,
        "R13": 13,
        "r14": 14,
        "R14": 14,
        "r15": 15,
        "R15": 15,
        "SCREEN": 16834,
        "KBD": 24576,
    }

    def __init__(self):
        self.__counter = 16

    def __contains__(self, symbol):
        return symbol in self.__SYM

    def add_entry(self, symbol: str, addr: int):
        self.__SYM[symbol] = addr

    def add_variable(self, symbol: str) -> int:
        self.__SYM[symbol] = self.__counter
        self.__counter += 1
        return self.__SYM[symbol]

    def get_addr(self, symbol: str) -> Optional[int]:
        return self.__SYM.get(symbol)

    def __repr__(self):
        return str(self.__SYM)
