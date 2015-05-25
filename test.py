#!/usr/bin/env python3

from icu import RuleBasedCollator
from sys import exit

RULES = ''
with open ("rules.txt", "r") as rulesfile:
    RULES=rulesfile.read()

COLLATOR = RuleBasedCollator('[normalization on]\n'+RULES)

EXIT_CODE = 0

# Very simple test function: we 
def testOrder(argList, testName):
    global EXIT_CODE
    argList = argList.split(' ')
    newList = sorted(argList, key=COLLATOR.getSortKey)
    if argList != newList:
        EXIT_CODE = 1
        print(testName+' ... FAIL!')
        print("expected ["+(", ".join(argList))+"]")
        print("got      ["+(", ".join(newList))+"]")
    else:
        print(testName+' ... OK')

# Tests corresponding to all the prefix+superscript+main+suffix+second suffix possibilities,
# see https://github.com/eroux/tibetan-spellchecker/blob/master/doc/standard-syllable-structure.md
testOrder("ཀ ཀྭ ཀྱ ཀྲ ཀླ དཀ དཀྭ དཀྱ དཀྲ དཀླ བཀ བཀྭ བཀྱ བཀྲ བཀླ རྐ རྐྱ ལྐ སྐ སྐྱ སྐྲ བརྐ བརྐྱ བསྐ བསྐྱ བསྐྲ", "letter ཀ")
testOrder("ཁ ཁྭ ཁྱ ཁྲ མཁ མཁྭ མཁྱ མཁྲ འཁ འཁྭ འཁྱ འཁྲ", "letter ཁ")
testOrder("ག གྭ གྱ གྲ གྲྭ གླ དགྭ དགྱ དགྲ དགྲྭ བགྭ བགྱ བགྲ བགྲྭ བགླ མགྭ མགྱ མགྲ མགྲྭ འགྭ འགྱ འགྲ འགྲྭ རྒ རྒྱ ལྒ སྒ སྒྱ སྒྲ བརྒ བརྒྱ བསྒ བསྒྱ བསྒྲ", "letter ག")
testOrder("ང རྔ ལྔ སྔ བརྔ བསྔ", "letter ང")
testOrder("ཅ ཅྭ གཅ གཅྭ བཅ བཅྭ", "letter ཅ")
testOrder("ཇ རྗ ལྗ བརྗ", "letter ཇ")
testOrder("ཉ ཉྭ གཉྭ མཉྭ རྙ སྙ བརྙ བསྙ", "letter ཉ")
testOrder("ཏ ཏྭ ཏྲ གཏྭ གཏྲ བཏྭ བཏྲ རྟ ལྟ སྟ བརྟ བལྟ བསྟ", "letter ཏ")
testOrder("ཐ ཐྲ", "letter ཐ")
testOrder("ད དྭ དྲ དྲྭ གདྭ བདྭ མདྭ འདྭ འདྲ འདྲྭ རྡ ལྡ སྡ བརྡ བལྡ བསྡ", "letter ད")
testOrder("ན རྣ སྣ སྣྲ བརྣ བསྣ", "letter ན")
testOrder("པ པྱ པྲ དཔྱ དཔྲ ལྤ སྤ སྤྱ སྤྲ", "letter པ")
testOrder("ཕ ཕྱ ཕྱྭ ཕྲ འཕྱ འཕྱྭ འཕྲ", "letter ཕ")
testOrder("བ བྱ བྲ བླ དབྱ དབྲ འབྱ འབྲ རྦ ལྦ སྦ སྦྱ སྦྲ", "letter བ")
testOrder("མ མྱ མྲ དམྱ དམྲ རྨ རྨྱ སྨ སྨྱ སྨྲ", "letter མ")
testOrder("ཙ ཙྭ གཙྭ བཙྭ རྩ རྩྭ སྩ བརྩ བརྩྭ བསྩ", "letter ཙ")
testOrder("ཚ ཚྭ མཚྭ འཚྭ", "letter ཚ")
testOrder("ཛ རྫ བརྫ", "letter ཛ")
testOrder("ཞ ཞྭ གཞྭ བཞྭ", "letter ཞ")
testOrder("ཟ ཟྭ ཟླ བཟྭ བཟླ", "letter ཟ")
testOrder("ར རྭ རླ བརླ", "letter ར")
testOrder("ཤ ཤྭ གཤྭ བཤྭ", "letter ཤ")
testOrder("ས སྭ སྲ སླ གསྭ བསྭ བསྲ བསླ", "letter ས")
testOrder("ཧ ཧྭ ཧྲ ལྷ", "letter ཧ")
testOrder("ཀི ཀུ ཀེ ཀོ", "standard vowels")
testOrder("ཀག ཀང ཀད ཀན ཀབ ཀམ ཀར ཀལ ཀས", "standard suffixes")
testOrder("ཀག ཀགས ཀང ཀངས ཀད ཀན ཀབ ཀབས ཀམ ཀམས ཀའ ཀའུ ཀར ཀལ ཀས", "standard and second suffixes")
testOrder("ཀག ཀགས ཀང ཀངས ཀད ཀན ཀབ ཀབས ཀམ ཀམས ཀའ ཀའང ཀའམ ཀའི ཀའིའོ ཀའུ ཀའུའང ཀའུའམ ཀའུའི ཀའུའིའོ ཀའུའོ ཀའོ ཀར ཀལ ཀས", "standard, second and grammatical suffixes")
# Test page 55 of Manuel de Tibétain Standard by Nicolas Tournadre
testOrder("ག་རེ་ གངས་ གི་ གིས་ གུར་ གེ་སར་ གོ་ གྭ་ གྱང་ གྱུར་ གྲང་མོ་ གྲངས་ གླ་ གླང་ དགའ་ དགུ་ དགེ་བ་ དགོས་ དགྲ་ བགམས་ བགེགས་ མགུར་ མགྱོགས་ རྒན་ རྒོད་པོ་ རྒྱ་ རྒྱ་མ་ ལྒང་བུ་ སྒ་ སྒུག་ སྒོར་མོ་ སྒྱུར་ སྒྲ་ བརྒལ་ བརྒྱ་ བསྒོམས་ བསྒྱུར་ བསྒྲགས་ བསིགྲགས་", "NT")
testOrder("གད་ གན་ གར་ གལ་ གས་ དག་ དང་ དབ་ དམ་ དར་ དལ་ དས་ བག བད་ བར་ བལ་ བས་ མག་ མད་ མབ་ མར་ མལ་ མས་", "2 syllables ambiguous")

exit(EXIT_CODE)
