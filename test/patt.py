#! /usr/bin/python -tt
def match (pattern,text):
	matches = []
	m = len(text)
	n = len(pattern)
	rightMostIndexes = BadCharacterShift(pattern)	
	alignedAt = 0
	while alignedAt + (n - 1) < m:
		for indexInPattern in xrange(n-1, -1, -1):
			indexInText = alignedAt + indexInPattern
			x = text[indexInText]
			y = pattern[indexInPattern]
			if indexInText >= m:
				break
			if x != y:
				r = rightMostIndexes.get(x)
				if x not in rightMostIndexes:
					alignedAt = indexInText + 1
				else:
					shift = indexInText - (alignedAt + r)
					alignedAt += (shift > 0 and shift or 1)
				break
			elif indexInPattern == 0:
				matches.append(alignedAt)
				alignedAt += 1

	return matches

def BadCharacterShift(pattern):
	map = { }
	for i in xrange(len(pattern)-1, -1, -1):
		c = pattern[i]
		if c not in map:
			map[c] = i
	return map

if __name__ == "__main__":
	matches = match("ll", "hello")
	for integer in matches:
		print "Match at:", integer
#	print (matches == [1, 3] and "OK" or "Failed")
