#!/bin/python3

import math
import os
import random
import re
import sys

class Multiset:

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return 0

if __name__ == '__main__':


## SAMPLE INPUT

# STDIN      Function
# -----      --------
# 12      →  number of queries, q = 12
# query 1 →  operations = ["query 1", "add 1", ..., "query 2", "size"]
# add 1
# query 1
# remove 1
# query 1
# add 2
# add 2
# size
# query 2
# remove 2
# query 2
# size

## SAMPLE OUTPUT

# False
# True
# False
# 2
# True
# True
# 1
