#!/bin/python3

import math
import os
import random
import re
import sys


def h(s):
    """ Cal the hash for the password"""
    p = 131
    m = pow(10, 9) +7

    tmp = 0
    s = s [::-1] # invert the string

    for i in range(len(s)):
        tmp += ord(s[i]) * pow(p, i)

    return int(tmp % m)


def authEvents(events):
    """ Create un array with the list of successed accesses (1) and failed ones (0)"""
    #print(events)

    hashPassword = 0
    successEvents = []

    for e in events:
        if e[0] == "setPassword":
            
            # calc the hash of the password
            password = e[1]
            hashPassword = h(password)
            #print(hashPassword)

        elif e[0] == "authorize":
            
            # check if the password can be accepted
            # this is the case in whitch the user insert the correct password + another character.
            # es. password = 'ABc01' - accepted password = 'ABc01a'
            # more information about ASCII table: https://ascii.cl/
            minHash = h(password + '0')
            maxHash = h(password + 'z')

            if e[1] == str(hashPassword): # correct hash
                successEvents.append(1)
            elif minHash >= int(e[1]) <= maxHash: # password witha a 1 more character at the end
                successEvents.append(1)
            else:
                successEvents.append(0)

    return successEvents


if __name__ == '__main__':

    events = [['setPassword', '000A'], ['authorize', '108738450'], ['authorize', '108738449'], ['authorize', '244736787']]

    result = authEvents(events)
    print(result)

