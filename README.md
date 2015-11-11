# String Set Matcher

String set matcher is a simple toolkit for finding the maximal match mapping
between two sets of strings.  This can be used to automatically map headers
between CSV-type data files, or for other similar purposes.

# Requirements

- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)

# Installation

    pip install string_set_matcher

# Usage

```python
>>>import string_set_matcher as ssm
```
#### match
```python
>>>ssm.match(frm, onto)
```
where `frm` and `onto` are strictly lists of python strings.

StringSetMatcher will attempt to match and provide scores for all possible
permutations of `frm` provided against `onto`,
returning results in a

    [ (mapping, score) ]

format, where "mapping" is an array such that

    mapping[i]

is the location that the `i`th element of `frm` mapped in `onto`.

