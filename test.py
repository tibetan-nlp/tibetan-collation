#!/usr/bin/env python3

from icu import RuleBasedCollator

RULES = ''
with open ("rules.txt", "r") as rulesfile:
    RULES=rulesfile.read()

COLLATOR = RuleBasedCollator('[normalization on]\n'+RULES)

EXIT_CODE = 0

# Very simple test function: we 
def testOrder(argList):
    print("Sorting ['"+("', '".join(argList))+"']...")
    newList = sorted(argList, key=COLLATOR.getSortKey)
    if argList == newList:
        EXIT_CODE = 1
        print("FAIL! got  ['"+("', '".join(argList))+"']")
    else:
        print('OK')

testOrder(('ད', 'བདག', 'བ'))
