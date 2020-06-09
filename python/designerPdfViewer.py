#!/bin/python3

import string

"""
When you select a contiguous block of text in a PDF viewer, the selection is 
highlighted with a bluerectangle. In this PDF viewer, each word is highlighted 
independently. For example, the highlighted text: 

abc def ghi

In this challenge, you will be given a list of letter heights in the alphabet 
and a string. Using the letterheights given, determine the area of the rectangle 
highlight in mm^2 assuming all letters are 1mm wide.

Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
"""

def designerPdfViewer(h, word):
    l = list(string.ascii_lowercase) # contain the array with all lowercase letter
    x = 0

    for i in range(len(word)):
        if h[l.index(word[i])] > x:
            x = h[l.index(word[i])]
            #print(f'h(i): {h[l.index(word[i])]}, x({i}) = {x}')
    
    print(len(word))
    return x * len(word)


# simple case 0
#h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
#word = 'abcz'

# simple case 1
#h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
#word = 'zaba'

h = [6, 5, 7, 3, 6, 7, 3, 4, 4, 2, 3, 7, 1, 3, 7, 4, 6, 1, 2, 4, 3, 3, 1, 1, 3, 5]
word = 'zbkkfhwplj'

result = designerPdfViewer(h, word)
print(result)


