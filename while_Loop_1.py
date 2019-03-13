# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:50:08 2017

@author: Reid
"""

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# added a comment just for git