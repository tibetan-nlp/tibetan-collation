#!/usr/bin/env python3

from icu import RuleBasedCollator
from sys import exit

RULES = ''
with open ("rules.txt", "r") as rulesfile:
    RULES=rulesfile.read()

COLLATOR = RuleBasedCollator('[normalization on]\n'+RULES)

EXIT_CODE = 0

# Very simple test function: we 
def testOrder(argList):
    global EXIT_CODE
    print("Sorting    ["+(", ".join(argList))+"]...")
    newList = sorted(argList, key=COLLATOR.getSortKey)
    if argList != newList:
        EXIT_CODE = 1
        print("FAIL! got  ["+(", ".join(newList))+"]")
    else:
        print('OK')

# Tests corresponding to all the prefix+superscript+main+suffix+second suffix possibilities,
# see https://github.com/eroux/tibetan-spellchecker/blob/master/doc/standard-syllable-structure.md
testOrder(("ཀ ཀྭ ཀྱ ཀྲ ཀླ དཀ དཀྭ དཀྱ དཀྲ དཀླ བཀ བཀྭ བཀྱ བཀྲ བཀླ རྐ རྐྱ ལྐ སྐ སྐྱ སྐྲ བརྐ བརྐྱ བསྐ བསྐྱ བསྐྲ").split(' '))
testOrder(("ཁ ཁྭ ཁྱ ཁྲ མཁ མཁྭ མཁྱ མཁྲ འཁ འཁྭ འཁྱ འཁྲ").split(' '))
testOrder(("དག བག མག འག").split(' '))
testOrder(("ག གྭ གྱ གྲ གྲྭ གླ དགྭ དགྱ དགྲ དགྲྭ བགྭ བགྱ བགྲ བགྲྭ བགླ མགྭ མགྱ མགྲ མགྲྭ འགྭ འགྱ འགྲ འགྲྭ རྒ རྒྱ ལྒ སྒ སྒྱ སྒྲ བརྒ བརྒྱ བསྒ བསྒྱ བསྒྲ").split(' '))
testOrder(("ང རྔ ལྔ སྔ བརྔ བསྔ").split(' '))
testOrder(("ཅ ཅྭ གཅ གཅྭ བཅ བཅྭ").split(' '))
testOrder(("ཇ རྗ ལྗ བརྗ").split(' '))
testOrder(("ཉ ཉྭ གཉྭ མཉྭ རྙ སྙ བརྙ བསྙ").split(' '))
testOrder(("ཏ ཏྭ ཏྲ གཏྭ གཏྲ བཏྭ བཏྲ རྟ ལྟ སྟ བརྟ བལྟ བསྟ").split(' '))
testOrder(("ཐ ཐྲ").split(' '))
testOrder(("ད དྭ དྲ དྲྭ གདྭ བདྭ མདྭ འདྭ འདྲ འདྲྭ རྡ ལྡ སྡ བརྡ བལྡ བསྡ").split(' '))
testOrder(("ན རྣ སྣ སྣྲ བརྣ བསྣ").split(' '))
testOrder(("པ པྱ པྲ དཔྱ དཔྲ ལྤ སྤ སྤྱ སྤྲ").split(' '))
testOrder(("ཕ ཕྱ ཕྱྭ ཕྲ འཕྱ འཕྱྭ འཕྲ").split(' '))
testOrder(("བ བྱ བྲ བླ དབྱ དབྲ འབྱ འབྲ རྦ ལྦ སྦ སྦྱ སྦྲ").split(' '))
testOrder(("མ མྱ མྲ དམྱ དམྲ རྨ རྨྱ སྨ སྨྱ སྨྲ").split(' '))
testOrder(("ཙ ཙྭ གཙྭ བཙྭ རྩ རྩྭ སྩ བརྩ བརྩྭ བསྩ").split(' '))
testOrder(("ཚ ཚྭ མཚྭ འཚྭ").split(' '))
testOrder(("ཛ རྫ བརྫ").split(' '))
testOrder(("ཞ ཞྭ གཞྭ བཞྭ").split(' '))
testOrder(("ཟ ཟྭ ཟླ བཟྭ བཟླ").split(' '))
testOrder(("ར རྭ རླ བརླ").split(' '))
testOrder(("ཤ ཤྭ གཤྭ བཤྭ").split(' '))
testOrder(("ས སྭ སྲ སླ གསྭ བསྭ བསྲ བསླ").split(' '))
testOrder(("ཧ ཧྭ ཧྲ ལྷ").split(' '))
# Test page 55 of Manuel de Tibétain Standard by Nicolas Tournadre
testOrder(("ག་རེ་ གངས་ གི་ གིས་ གུར་ གེ་སར་ གོ་ གྭ་ གྱང་ གྱུར་ གྲང་མོ་ གྲངས་ གླ་ གླང་ དགའ་ དགུ་ དགེ་བ་ དགོས་ དགྲ་ བགམས་ བགེགས་ མགུར་ མགྱོགས་ རྒན་ རྒོད་པོ་ རྒྱ་ རྒྱ་མ་ ལྒང་བུ་ སྒ་ སྒུག་ སྒོར་མོ་ སྒྱུར་ སྒྲ་ བརྒལ་ བརྒྱ་ བརྒོམས་ བསྒྱུར་ བསྒྲགས་ བསིགྲགས་").split(' '))
# There are mistakes in it. Fixed version:
#testOrder(("ག་རེ་ གངས་ གི་ གིས་ གུར་ གེ་སར་ གོ་ གྭ་ གྱང་ གྱུར་ གྲང་མོ་ གྲངས་ གླ་ གླང་ དགའ་ དགུ་ དགེ་བ་ དགོས་ དགྲ་ བགམས་ བགེགས་ མགུར་ མགྱོགས་ རྒན་ རྒོད་པོ་ རྒྱ་ རྒྱ་མ་ ལྒང་བུ་ སྒ་ སྒུག་ སྒོར་མོ་ སྒྱུར་ སྒྲ་ བརྒལ་ བརྒྱ་ བརྒོམས་ བསྒྱུར་ བསྒྲགས་ བསིགྲགས་").split(' '))

exit(EXIT_CODE)
