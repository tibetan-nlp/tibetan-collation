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
    print("Sorting    ['"+("', '".join(argList))+"']...")
    newList = sorted(argList, key=COLLATOR.getSortKey)
    if argList != newList:
        EXIT_CODE = 1
        print("FAIL! got  ['"+("', '".join(newList))+"']")
    else:
        print('OK')

testOrder(['ད', 'བདག', 'བ'])
testOrder(("ཀ ཀྭ ཀྱ ཀྲ ཀླ དཀ དཀྭ དཀྱ དཀྲ དཀླ བཀ བཀྭ བཀྱ བཀྲ བཀླ རྐ རྐྱ ལྐ སྐ སྐྱ སྐྲ བརྐ བརྐྱ བསྐ བསྐྱ བསྐྲ").split(' '))
testOrder(("ཁ ཁྭ ཁྱ ཁྲ མཁ མཁྭ མཁྱ མཁྲ འཁ འཁྭ འཁྱ འཁྲ").split(' '))
testOrder(("ག གྭ གྱ གྲ གྲྭ གླ དག དགྭ དགྱ དགྲ དགྲྭ བག བགྭ བགྱ བགྲ བགྲྭ བགླ མག མགྭ མགྱ མགྲ མགྲྭ འག འགྭ འགྱ འགྲ འགྲྭ རྒ ལྒ སྒ རྒྱ སྒྱ སྒྲ བརྒ བསྒ བརྒྱ བསྒྱ བསྒྲ").split(' '))
testOrder(("ང དང མང རྔ ལྔ སྔ བརྔ བསྔ").split(' '))
testOrder(("ཅ ཅྭ གཅ གཅྭ བཅ བཅྭ").split(' '))
testOrder(("ཆ མཆ འཆ").split(' '))
testOrder(("ཇ མཇ འཇ རྗ ལྗ བརྗ").split(' '))
testOrder(("ཉ ཉྭ གཉ གཉྭ མཉ མཉྭ རྙ སྙ བརྙ བསྙ").split(' '))
testOrder(("ཏ ཏྭ ཏྲ གཏ གཏྭ གཏྲ བཏ བཏྭ བཏྲ རྟ ལྟ སྟ བརྟ བལྟ བསྟ").split(' '))
testOrder(("ཐ ཐྲ མཐ འཐ").split(' '))
testOrder(("ད དྭ དྲ དྲྭ གད གདྭ བད བདྭ མད མདྭ འད འདྭ འདྲ འདྲྭ རྡ ལྡ སྡ བརྡ བལྡ བསྡ").split(' '))
testOrder(("ན གན མན རྣ སྣ སྣྲ བརྣ བསྣ").split(' '))
testOrder(("པ པྱ པྲ དཔ དཔྱ དཔྲ ལྤ སྤ སྤྱ སྤྲ").split(' '))
testOrder(("ཕ ཕྱ ཕྱྭ ཕྲ འཕ འཕྱ འཕྱྭ འཕྲ").split(' '))
testOrder(("བ བྱ བྲ བླ དབ དབྱ དབྲ འབ འབྱ འབྲ རྦ ལྦ སྦ སྦྱ སྦྲ").split(' '))
testOrder(("མ མྱ མྲ དམ དམྱ དམྲ རྨ སྨ རྨྱ སྨྱ སྨྲ").split(' '))
testOrder(("ཙ ཙྭ གཙ གཙྭ བཙ བཙྭ རྩ རྩྭ སྩ བརྩ བརྩྭ བསྩ").split(' '))
testOrder(("ཚ ཚྭ མཚ མཚྭ འཚ འཚྭ").split(' '))
testOrder(("ཛ མཛ འཛ རྫ བརྫ").split(' '))
testOrder(("ཞ ཞྭ གཞ གཞྭ བཞ བཞྭ").split(' '))
testOrder(("ཟ ཟྭ ཟླ གཟ བཟ བཟྭ བཟླ").split(' '))
testOrder(("ར རྭ རླ བརླ").split(' '))
testOrder(("ཤ ཤྭ གཤ གཤྭ བཤ བཤྭ").split(' '))
testOrder(("ས སྭ སྲ སླ གས གསྭ བས བསྭ བསྲ བསླ").split(' '))
testOrder(("ཧ ཧྭ ཧྲ ལྷ").split(' '))

exit(EXIT_CODE)
