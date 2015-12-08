#! /usr/bin/python -tt
import os
def highalert(strn):
	if int(strn)<100:
		print int(strn)
		os.system("echo ' high elert strn ' >>alertfile")
		os.system("xmessage -file alertfile &")
def main():
	highalert('0092')
if __name__=='__main__':
	main()

