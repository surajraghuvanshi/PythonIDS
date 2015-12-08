#! /usr/bin/python -tt
def loadSign():
	f=open('tcp','r')
	lines=f.readlines()
	for line in lines:
		splited= line.split(', ')
		first=splited[0]
		second=splited[1]
		thiredpre=splited[2]
		thired=thiredpre[3:]
		fourth=splited[3]
		fifthpre=splited[4]
		fifth=fifthpre[5:-1]
		sixthpre=splited[5]
		sixth=sixthpre[9:-1]
		saventhpre=splited[6]
		saventh=saventhpre[4:-1]
		if sixth.startswith('|'):
			sixthprefinal=sixthpre[10:-2]
			sixthsecondfinal=sixthprefinal.replace(' ','')
			print sixthsecondfinal
			sixthfinal=sixthsecondfinal.encode('hex')
		else:
			sixthfinal=sixth.encode('hex')
#		print type(second)
		list1 =[first,second,thired,fifth,sixthfinal,saventh]
		return list
		print first , second, thired, fourth, fifth, sixthfinal, saventh
		print 
def main():
	loadSign()
if __name__=='__main__':
	main()
