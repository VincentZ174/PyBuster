import socket
import requests
import argparse
import sys 

def DNSMode(wordlist, domain_name):

	for subdomain in wordlist:
		
		url = f"{subdomain}.{domain_name}"
		try:
			addr = socket.gethostbyname(url)
			print(f"[+] {url}")
		except:
			pass

def VHOSTMode(wordlist, domain_name):

	for subdomain in wordlist:
		url = f"https://{subdomain}.{domain_name}"

		try:

			r = requests.get(url, timeout=5)
			status_code = r.status_code
			size = len(r.content)
			print(f"[+] {url} ({status_code}) [Size: {size}]")

		except requests.ConnectionError:
			pass
		except requests.exceptions.TooManyRedirects:
			print(f"[+] {url} ({status_code}) [Size: {size}]")
		except KeyboardInterrupt:
			sys.exit()

def DIRMode(wordlist, domain_name):
	for directory in wordlist:
			url = f"https://www.{domain_name}/{directory}"

			try:

				r = requests.get(url)
				status_code = r.status_code
				size = len(r.content)
				print(f"[+] {url} ({status_code}) [Size: {size}]")

			except requests.ConnectionError:
				pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser(usage = "python3 URIDiscovery.py -m [MODE] -w [path/to/wordlist]", formatter_class = argparse.RawTextHelpFormatter)
	parser.add_argument("-m", "--mode", required = True, 
	help = """dir    Directory/file bruteforce mode\nDNS    subdomain bruteforce mode\nVHOST  bruteforce mode""")
	parser.add_argument("-u", "--url", required = True, help = "Address of Website")
	parser.add_argument("-w", "--wordlist", required = True, help = "Path to wordlist")
	args = parser.parse_args()

	with open(args.wordlist, 'r') as file:
		
		name = file.read()

		wordlist = name.splitlines()
	try:
		if args.mode.lower() == "dir":
			DIRMode(wordlist, args.url)
		elif args.mode.lower() == "vhost":
			VHOSTMode(wordlist, args.url)
		else:
			DNSMode(wordlist, args.url)
	except KeyboardInterrupt:
		sys.exit()



