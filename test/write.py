#! /usr/bin/python -tt
def write(alerttype,ip1, port1, ip2, port2,msg):
	if alerttype=='TCP':
		alertfile='TcpAlert'
	else:
		alertfile='IpAlert'
	file=open(alertfile, 'a+')
	message=msg
	ip1='192.168.1.2 '
	port1="80 "
	ip2='192.168.1.1 '
	port2="8080 "
	alert=['source address:=> ',ip1,'source port:=> ',port1,'destination address:=> ',ip2,'destination port:=> ',port2,'message:=>',message]
	print alert
	for data in alert:
		file.write(data)
	file.write('\n ==============================================================================================\n')	
#	function to call email generation alert
#	mail()	
#	file.write('hello2 \n')
def main():
	print 'hello'
	alerttype='IP'
	ip='192.168.1.2 '
	mac="80 "
	ip='192.168.1.1 '
	mac="80 "
	msg='type of alert '
	write(alerttype,ip, mac, ip, mac,msg)
if __name__=='__main__':
	main()
