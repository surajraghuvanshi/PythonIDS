#! /usr/bin/python -tt
def search(sourceip, destinationip,sourceport, destinationport,payloadhex):
	print sourceip
	print sourceport
	print destinationip
	print destinationport
	f=open('signature','r')
	lines=f.readlines()
	for line in lines:
		splited= line.split(' (')
		first=splited[0]
		second=splited[1]
		secondsplit=first.split()
		source_ip=secondsplit[2]
		source_port=secondsplit[3]
		desti_ip=secondsplit[5]
		desti_port=secondsplit[6]
		thiredsplit=second.split(';')
		premsg=thiredsplit[0]
		precontent=thiredsplit[1]
		presid=thiredsplit[2]
		msg=premsg[5:-1]
		sid= presid[5:-2]
		if precontent[10:-1].startswith('|'):
			secondcontent=precontent[11:-2].replace(' ','')
			content=secondcontent.encode('hex')
		else:
			content=precontent[10:-1].encode('hex')
def main():
	search()
if __name__=='__main__':
	main()
