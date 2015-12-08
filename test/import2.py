#! /usr/bin/python -tt
import import1
def second():
#	print 'hello import2 second'
	import1.first()
def main():
	second()
if __name__=='__main__':
	main()
