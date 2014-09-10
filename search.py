#! /usr/bin/python -tt
# import the Pattern Matching Program that will be called for signature matching in the data payload
# import alertgeneration that will be used for generating the alert(alert will be write in the AlertFile ) 
import PatternMatching
import alertgeneration
# Define the function search this function is called by the PacketCaptureandDecode program it will take five parameter
# those are source ip , Destination ip, source port, destination port and data payload that data payload is in the form og hex string 
def search(protocol,sourceip, destinationip,sourceport, destinationport,payloadhex):
	print '==============================================================================='
	s_ip=sourceip
	d_ip=destinationip
# define Internal and External network Based on the IP range
	if sourceip=='192.168.1.1':
		sourceiptoMatch='$HOME_NET'
		destinationiptomatch='$EXTERNAL_NET'
	else:
		sourceiptoMatch='$EXTERNAL_NET'
		destinationiptomatch='$HOME_NET'
# Load the signature form signature file that is opened in read mode only
# Define a object fileopen of file reader class
	if protocol==6:
		signaturefile='TCPSignature'
	elif protocol==17:
		signaturefile='UDPSignature'
	else:
		signaturefile='ICMPSignature'
	fileopen=open(signaturefile,'r')
	lines=fileopen.readlines()
# start Reading line by line
	for line in lines:
# split the string that are recived from signature file and find values of Soure ip source port destination ip destination port 
# message and the malicious content in form of signature 
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
		if sourceiptoMatch==source_ip and destinationiptomatch==desti_ip:
			matches=PatternMatching.match(content,payloadhex)
			if matches!=[]:
# Calling the function write from the imported class alergeneration it also take eight arguments 
# and generate a alert and write it into the Alertfile
				alertgeneration.write(s_ip, sourceport, d_ip, destinationport, msg,sid)		
# define main function
def main():
	search()
if __name__=='__main__':
	main()
