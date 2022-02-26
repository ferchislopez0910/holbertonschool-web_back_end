#!/usr/bin/env python3
'''Annotate the below function’s
parameters and return values with
the appropriate types
Arguments: lst: Iterable[Sequence]
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return list of tuples
    '''
    return [(i, len(i)) for i in lst]