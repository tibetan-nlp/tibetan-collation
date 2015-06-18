# Standard tibetan sorting

Tibetan use a specific sorting algorithm, described here in a human understandable form. The presented algorithm is only correct for syllables following the [standard tibetan syllable structure](https://github.com/eroux/tibetan-spellchecker/blob/master/doc/standard-syllable-structure.md).

## Algorithm for standard Tibetan

These lines only apply to standard Tibetan syllables. For sorting words, you can just sort syllable by syllable.

The first order of sorting is the main consonnant of the syllable.

If they are equal, then the order goes as follows:

- superscript
- prefix
- subscript
- vowel
- suffix

### Order of superscripts

The subscript letters sort in the following order (presented above ཀ):

- ཀ (no superscript)
- རྐ
- ལྐ
- སྐ

### Order of prefixes

The prefix letters sort in the following order:

- no prefix
- ག
- ད
- བ
- མ
- འ

### Order of subscripts

The subscript letters sort in the following order (presented on ཀ):

- ཀ (no subscript)
- ཀྭ
- ཀྱ
- ཀྱྭ
- ཀྲ
- ཀྲྭ
- ཀླ
- ཀླྭ

### Order of vowels

The vowels sort in the following order (presented on ཀ):

- ཀ (no vowel)
- ཀི
- ཀུ
- ཀེ
- ཀོ

### Order of suffixes

Suffixes are sorted in following order:

- (no suffix)
- ག
- གས
- ང
- ངས
- ད
- ན
- བ
- བས
- མ
- མས
- འ
- འང
- འམ
- འི
- འིའང
- འིའམ
- འིའི
- འིའིས
- འིའོ
- འིར
- འིས
- འུ
- འུའང
- འུའམ
- འུའི
- འུའིས
- འུའོ
- འུར
- འུས
- འོ
- འོའང
- འོའམ
- འོའི
- འོའིས
- འོའོ
- འོར
- འོས
- ར
- ལ
- ས
