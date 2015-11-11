# simple program to determine the best match for a set of strings.
# depends on the fuzzywuzzy string matching package.
# by default performs an exhaustive enumeration of the search space.

from fuzzywuzzy import fuzz
import itertools

def gen_elem_scores(f,o):
    if f is not None and o is not None:
        return fuzz.ratio(f,o)
    else:
        return 0

# takes two string sets and returns a score.
def score_set_match(frm, onto):
    score = sum( map(gen_elem_scores, frm, onto) )
    return score

# function taking two lists of strings and returning a list of tuples
# of the form:
#
#    [ (mapping, score) ]
#
# which will allow the calling program to determine what to do.
def map_string_sets(frm, onto):
    perm_gen = itertools.permutations(frm)
    for perm in perm_gen:
        print score_set_match(perm, onto)
        print str(perm) + " -> " + str(onto);

map_string_sets(['name', 'change', 'depth'], ['full name', 'change type', 'deepness'])

