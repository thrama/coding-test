#!/bin/python3

import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    l = list(string.ascii_lowercase) # contain the array with all lowercase letter
    x = 0

    for i in range(len(word)):
        if l.index(word[i]) > x:
            x = h[l.index(word[i])]
    
    return x * len(word)


# simple case 0
#h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
#word = 'abcz'

# simple case 1
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = 'zaba'

result = designerPdfViewer(h, word)
print(result)


