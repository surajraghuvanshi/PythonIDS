#!/usr/bin/env python
#original Boyer-Moore implementor (v1): Shriphani Palakodety

import time

bcs = {} #the table

def goodSuffixShift(key):
    for i in xrange(len(key)-1, -1, -1):
      if key[i] not in bcs.keys():
        bcs[key[i]] = len(key)-i-1


#---------------------- v1 ----------------------
def searchv1(text, key):
    #base from Shriphani Palakodety fixed for single char
    i = len(key)-1
    index = len(key) -1
    j = i 

    while True:
        if i < 0:
            return j + 1
        elif j > len(text):
            return "not found"
        elif text[j] != key[i] and text[j] not in bcs.keys():
            j += len(key)
            i = index
        elif text[j] != key[i] and text[j] in bcs.keys():
            j += bcs[text[j]]
            i = index
        else:
            j -= 1
            i -= 1

#---------------------- v2 ----------------------                        
def searchv2(text, key):
    #removed string len functions from loop
    len_text = len(text)
    len_key = len(key)
    i = len_key-1
    index = len_key -1
    j = i

    while True:
      if i < 0:
        return j + 1
      elif j > len_text:
        return "not found"
      elif text[j] != key[i] and text[j] not in bcs.keys():
        j += len_key
        i = index
      elif text[j] != key[i] and text[j] in bcs.keys():
        j += bcs[text[j]]
        i = index
      else:
        j -= 1
        i -= 1                        

#---------------------- v3 ----------------------
def searchv3(text, key):
    #from v2 plus modified 3rd if condition - breaking down the comparison for efficency,
    #modified the while loop to include the first if condition (oppposite of it)
    len_text = len(text)
    len_key = len(key)
    i = len_key-1
    index = len_key -1
    j = i

    while i >= 0 and j <= len_text:
      if text[j] != key[i]:
            if text[j] not in bcs.keys():
                j += len_key
                i = index
            else:
                j += bcs[text[j]]
                i = index
    else:
        j -= 1
        i -= 1

    if j > len_text:
        return "not found"
    else:
        return j + 1


key_list = ["POWER", "HOUSE", "COMP", "SCIENCE", "SHRIPHANI", "BRUAH", "A", "H"]

text = "SHRIPHANI IS A COMPUTER SCIENCE POWERHOUSE"

t1 = time.clock()
for key in key_list:
    goodSuffixShift(key)
    #print searchv1(text, key)
    searchv1(text, key)
    bcs = {}
t2 = time.clock()
print 'v1 took %0.5f ms' % ((t2-t1)*1000.0)

t1 = time.clock()
for key in key_list:
    goodSuffixShift(key)
    #print searchv2(text, key)
    searchv2(text, key)
    bcs = {}

t2 = time.clock()
print 'v2 took %0.5f ms' % ((t2-t1)*1000.0)
