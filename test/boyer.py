#!/usr/bin/python -tt
import time
bcs = {} #the table
def goodSuffixShift(key):
    for i in xrange(len(key)-1, -1, -1):
      if key[i] not in bcs.keys():
        bcs[key[i]] = len(key)-i-1
#--------------------------------------------
def search(text, key):
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
#            print "find key",key, "at index",index
        elif text[j] != key[i] and text[j] in bcs.keys():
            j += bcs[text[j]]
            i = index
            print "find key",key, "at index",index
        else:
            j -= 1
            i -= 1
#def main():
key_list = ["POWER", "HOUSE", "COMP", "SCIENCE", "SHRIPHANI", "BRUAH", "A", "H"]
text = "SHRIPHANI IS A COMPUTER SCIENCE POWERHOUSE"
t1 = time.clock()
for key in key_list:
    goodSuffixShift(key)
    search(text, key)
    bcs = {}
print bcs
t2 = time.clock()
print 'its took %0.5f s' % ((t2-t1)*100000.0)
#if __name__=='__main__':
#	main()
