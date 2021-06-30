#!/usr/bin/env python3
"""Fix the font names for the variable fonts"""
# TODO (M Foley) this shouldn't be required. Send fix to fontmake
from fontTools.ttLib import TTFont
from glob import glob
import os

font_paths = glob("fonts/variable/*.ttf")

for path in font_paths:
    font = TTFont(path)
    font["name"].setName("Josefin Sans", 1, 3, 1, 1033)
    if "Italic" in str(path):
        font["name"].setName("Italic", 2, 3, 1, 1033)
        font["name"].setName("UCT;JosefinSans-Italic", 3, 3, 1, 1033)
        font["name"].setName("Josefin Sans Italic", 4, 3, 1, 1033)
        font["name"].setName("JosefinSans-Italic", 6, 3, 1, 1033)
        font["name"].setName("Josefin Sans", 16, 3, 1, 1033)
        font["name"].setName("Italic", 17, 3, 1, 1033)
    else:
        font["name"].setName("Regular", 2, 3, 1, 1033)
        font["name"].setName("UCT;JosefinSans-Regular", 3, 3, 1, 1033)
        font["name"].setName("Josefin Sans Regular", 4, 3, 1, 1033)
        font["name"].setName("JosefinSans-Regular", 6, 3, 1, 1033)
        font["name"].setName("Josefin Sans", 16, 3, 1, 1033)
        font["name"].setName("Regular", 17, 3, 1, 1033)

    font.save(path + ".fix")
