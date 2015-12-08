#! /usr/bin/python -tt
import PatternMatching
def start():
#	print 'start'
	matches=PatternMatching.match("a","hello")
#	print matches
	if matches==[]:
		print 'no match'
	else:
		print 'matches at ', matches
def main():
	start()
if __name__=='__main__':
	main()

