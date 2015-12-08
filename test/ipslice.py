#! /usr/bin/python -tt
def slice():
#	print 'hello function'
	ip='192.168.1.4'
	ipslice=ip[:9]
	print ipslice
	if ipslice=='192.168.1':
		ipsource='INT_NET'
		ipdestination='EXT_NET'
	else:
		ipsource='EXT_NET'
		ipdestination='INT_NET'
	print ipsource ,':=>',ipdestination
	abc=['hello','world','content',123456]
	print type(abc[2])
	print abc
def main():
	print 'hello main'
	slice()
if __name__=='__main__':
	main()
