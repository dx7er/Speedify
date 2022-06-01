import os
import argparse, pyfiglet
from speedtest import Speedtest

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


netsp=Speedtest()

os.system('clear')
baner=pyfiglet.figlet_format("speedify")

print(CYAN,baner,end=' ')
print(GREEN,'\t\t\t\t by naqviO7')

def SpeedTest(args):
	print(BLUE)
	print('[+] Choosing Best Server.')
	bestserver=netsp.get_best_server()
	print(f"[+] Best Server is: {bestserver['host']} in {bestserver['country']}")

	print('[+] Preforming Download Speed Test.')
	download_result=netsp.download()

	print('[+] Preforming Upload Speed Test.')
	upload_result=netsp.upload()
	ping_result=netsp.results.ping

	print(CYAN)
	if args.sp=='start':
		print('\n---------------------- Scan Results ----------------------')
		print(f"[!] Download Speed: {download_result/1024/1024:.2f} Mbits/s")
		print(f"[!] Upload Speed: {upload_result/1024/1024:.2f} Mbits/s")
		print(f"[!] Ping: {ping_result:.2f} ms")
		print('----------------------------------------------------------\n')
	else:
		print('Arguement not Given Correctly!\n')


if __name__=='__main__':

	parser=argparse.ArgumentParser(description='Speed Test Utility Written in Python!')
	parser.add_argument('-sp',type=str,help='Speed Test Scan!')
	args=parser.parse_args()

	SpeedTest(args)
