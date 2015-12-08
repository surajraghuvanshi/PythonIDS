#! /usr/bin/python -tt
import sys
def readfile():
	print 'hello1'
	file=open('virussign','r')
#	print file
	for line in open('myfile','r'):
        abc=file.readl()
        print abc
#	abc1()
def abc1():
	with open('virussign', 'r') as fin:
		output=fin.read()
		print output
#		signature[0]=output[0]
def main():
	print 'hello'
	read()
if __name__=='__main__':
	main()
