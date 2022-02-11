import os
import argparse, pyfiglet
from speedtest import Speedtest

netsp=Speedtest()

os.system('cls')
baner=pyfiglet.figlet_format("speedify")

print(baner,end=' ')
print('\t\t\t\t by naqviO7')

def SpeedTest(args):
	print('[+] Choosing Best Server.')
	bestserver=netsp.get_best_server()
	print(f"[+] Best Server is: {bestserver['host']} in {bestserver['country']}")

	print('[+] Preforming Download Speed Test.')
	download_result=netsp.download()

	print('[+] Preforming Upload Speed Test.')
	upload_result=netsp.upload()
	ping_result=netsp.results.ping
	
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
