#! /usr/bin/python -tt
# import os module to execute system commands
import os
# Define the function that will take eight arguments these are alert type that is tcp only at here
# this function is called by search function if the virus signature is matched in the data payload 
# arguments are alert type that can be tcp , ip udp, http, for further ammendment, 
def write(source_ip, source_port, desti_ip, desti_port,msg,sid):
	file=open('Alertfile', 'a+')
	message=msg
	uid=sid
	alert=['sid: ',uid,' Source ip: ',source_ip,' source_port: ',source_port,' destination ip: ',desti_ip,' destination port: ',desti_port,' msg: ',msg]
#	print alert
	for data in alert:
		file.write(data)
	file.write('\n ------------------------------------------------------------------------------------------------------------------------------------\n')	
	if int(uid)<100:
		highalert()
# define the function to send mail if the alert is very criticle
# highalert function called a utulity xmessage to display the message
def highalert():
# execute a system command to pop-up message 
	os.system("xmessage 'high alert is found please check the Alertfile' -nearmouse -timeout 5")
#	os.system('command to send mail')
#	function to call email generation alert
#	mail()	
