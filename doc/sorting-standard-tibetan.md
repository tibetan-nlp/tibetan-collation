# Standard tibetan sorting

Tibetan use a specific sorting algorithm, described here in a human understandable form. The presented algorithm is only correct for syllables following the [standard tibetan syllable structure](https://github.com/eroux/tibetan-spellchecker/blob/master/doc/standard-syllable-structure.md).

The algorithm sorts according to 6 weights in the following order:

- main consonnant
- superscript
- prefix
- subscript
- vowel
- suffix

See below for the sorting order inside each weight.

## Examples

Let's take a few examples:

Comparing མགད and མག: in the first one, the main consonnant is ག, in the second one, the main consonnant is མ, they differ on the first weight, so we have མགད < མག du to the order of the main consonnant.

Comparing བསྒ and མགོ: the main consonnants are the same (ག), so we compare the second weight. The first one has superscript ས, the second has no superscript, so according the order of superscripts, བསྒ > མགོ.

Comparing འགྲ and འགྱི: the main consonnants are the same (ག), the superscripts are the same (no superscript), the prefix are the same (འ), so we compare the fourth weight. The first has subscript ར, the second has subscript ཡ, so according to the order of subscript, we have འགྱི < འགྲ.

Comparing མགུ and མག: the main consonnants are the same (ག), the superscripts are the same (no superscript), the prefix are the same (མ), the subscripts are the same (no subscript), so we compare the fifth weight. The first has vowel u, the second has no vowel, so according to the order ofvowel, we have མགུ > མག.

Comparing དགར and དགལ: the main consonnants are the same (ག), the superscripts are the same (no superscript), the prefix are the same (ད), the subscripts are the same (no subscript), the vowels are the same (no vowel), so we compare the sixth weight. The first has suffix ར, the second has suffix ལ, so according to the order of suffixes, we have དགར < དགལ.

## Implementation

This algorithm could be easily implemented using the same mechanism as [UCA](http://unicode.org/reports/tr10/).

## Order Listing

### Order of main consonnant

The main consonnants sort in the following order:

  - ཀ
  - ཁ
  - ག
  - ང
  - ཅ
  - ཆ
  - ཇ
  - ཉ
  - ཏ
  - ཐ
  - ད
  - ན
  - པ
  - ཕ
  - བ
  - མ
  - ཙ
  - ཚ
  - ཛ
  - ཝ
  - ཞ
  - ཟ
  - འ
  - ཡ
  - ར
  - ལ
  - ཤ
  - ས
  - ཧ
  - ཨ

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
