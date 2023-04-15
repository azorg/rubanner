#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Программа аналогичная "System-V banner clone" на Pytnon3 с кирилицей.
# Использьуется шрифт 6*8, который когда-то использовал на ZX Spectrum.

import sys
from font_6x8 import font_6x8 as FONT

PIXEL_1="#"
PIXEL_0=" "

# put word (6x8 font) on stdout
def put_word(text):
    for i in range(1, 8):
        for uchr in text:
            sym = FONT[ord(uchr)]
            for j in range(6):
                print((PIXEL_1 if (sym[j] & (0x80 >> i)) else PIXEL_0), end="")
        print()
    print()

for word in sys.argv[1:]:
    put_word(word)


