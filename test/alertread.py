#! /usr/bin/python -tt
def fileread():
	print 'hello'
	string='"192.168.1.1" , "80","192.168.1.3","90"'
	string1='"192.168.1.1" , "80","192.168.1.3","90",hello world welcome here |00 23 a4 09 57 ac c3| this is the context here it may contain malacious content like 00 00 00 00 00 that is used for backdoor entry in the window operating system or like 01 01 01 01 01 that may be used for linux exploitation '
#	abc=string1.find("00 00 00")	
	print string
	tosearch=["00 00 00 00","backdoor","01 01 01 01","linux","surajpratap"]
	for element in tosearch:
#		print string1.find(element)
		if string1.find(element)==-1 :
			print "no match for the element" ,'"',element,'"'
		else:
			print "program has found a match for the string",'"',element,'"',"at location ",string1.find(element)
#	print abc
#	print string1
def main():
	fileread()
if __name__=='__main__':
	main()
