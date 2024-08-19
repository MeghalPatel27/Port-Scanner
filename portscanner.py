import socket
import termcolor

def scan(target,ports):
	print( '\n'+ " Starting Scan for " + target)
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress,port):
	try:
		sock=socket.socket()
		sock.connect((ipaddress,port))
		print("[+] Port Open " + str(port))
		sock.close()
	except:
		pass

targets=input("[*] Enter targets to Scan (split them by ,) : ")
ports=int(input("[*] Enter how many ports you want to scan : "))

if ',' in targets:
	print(termcolor.colored("\n Scanning Multiple targets",'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '),ports)
		print('\n'+ " End Scan for "+ ip_addr)


else:
	scan(targets,ports)
	print('\n' + " End Scan for "+ targets)
