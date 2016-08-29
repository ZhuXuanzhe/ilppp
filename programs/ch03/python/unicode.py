"""
A program using Unicode regexes
Usage: python unicode.py
"""
__author__ = "Pierre Nugues"

import regex as re

alphabet = 'αβγδεζηθικλμνξοπρστυφχψω'
match = re.search('^\p{InBasic_Latin}+$', alphabet)
print(match)  # None
match = re.search('^\p{InGreek_and_Coptic}+$', alphabet)
print(match)  # matches alphabet
match = re.search('^\p{Greek}+$', alphabet)
print(match)  # matches alphabet
match = re.search('\N{GREEK SMALL LETTER ALPHA}', alphabet)
print(match)  # matches 'α'
match = re.search('α', alphabet)
print(match)  # matches 'α'
