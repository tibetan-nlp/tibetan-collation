#!/usr/bin/env python3

from icu import RuleBasedCollator

rules = ''
with open ("rules.txt", "r") as myfile:
    rules=myfile.read()

print(rules)

collator = RuleBasedCollator('[normalization on]\n'+rules)

print(sorted(['བ', 'བད', 'ད'], key=collator.getSortKey))
