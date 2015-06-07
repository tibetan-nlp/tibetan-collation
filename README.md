# Testing and improving Tibetan collation

This repository provides tests and improvements of Tibetan sorting.

It currently uses one backend:

- the [Unicode Collation Algorithm](http://unicode.org/reports/tr10/) (UCA)


To use it, you must install Python 3 and [PyICU](http://pyicu.osafoundation.org/).

To run the tests, simply run `./test.py`.

See [ICU doc](http://userguide.icu-project.org/collation/customization) and [Unicode doc](http://www.unicode.org/reports/tr35/tr35-collation.html#Orderings) for rule file format.

## History
