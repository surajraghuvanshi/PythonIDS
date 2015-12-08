import sys
import re
def fileread()
    file = open(/root/IDS/virusSignature/virussign,'r')
    while 1:
    line = file.readline()
        print line
    if not line:
        break
        print 'end'
    file.close()
if __name__==__main__:
    fileread()
