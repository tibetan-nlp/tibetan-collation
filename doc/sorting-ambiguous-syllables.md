# Standard tibetan sorting

Tibetan has 8 ambiguous syllables where it is not possible to know what the main stack is. This is documented [here](https://github.com/eroux/tibetan-spellchecker/blob/master/doc/standard-syllable-structure.md). A collation algorithm should treat these syllables as their most common form, documented in the above link. Still, there might be (extremely rare) cases where a user might want to treat one of these syllables. 

### Specify first consonnant as main

Let's take the case of དམས་: in normal cases, it should be treated as having མ as main consonnant. But if you want to treat is as having ད as main consonnant, you must use Unicode character U+034F COMBINING GRAPHEME JOINER (hereafter referenced as *CGJ*) after ད. The use of this character is documented [here](http://unicode.org/reports/tr10/#Combining_Grapheme_Joiner). Any collation algorithm should handle it properly.

A collation algorithm should respect the following order:

    ད་ དམ་ ད͏མས་ གདའ་ མ་ དམར་ དམས་ དམི་

(the first དམས་ contains a CGJ: དCGJམས་).

### Specify second consonnant as main

The same mechanism cannot be used to specify the second consonnant as the main one, there seems to be no clear canonical mechanism to do so. What we propose here is to use Unicode character U+200B ZERO WIDTH SPACE (hereafter referenced as *ZWSP*) after the second stack. Unlike the other solution, this is not canonical, and all collation algorithm might not supported (the rules provided in this repository should).

A collation algorithm implementing this method should respect the following order:

 ​   ང་ མངར་ མང​ས་ མངི་ མ་ མང་ མངས་ མད་

(the first མངས་ contains a ZWSP: མངZWSPས་)
