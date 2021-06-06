import pyfiglet
import argparse
import urllib.request
import requests
def banner():
	banner = pyfiglet.figlet_format("WELCOME!")
	print(banner)
	print("""
                         #CODE BY-AMRITA NAYAK


		""")
	arguments()
def arguments():
	parser = argparse.ArgumentParser()
	#parser.add_argument('--h', dest='help', type=str, help='Helping menu')
	parser.add_argument('-u', dest='URL' ,help='Specify Your URL')
	parser.add_argument('-w', dest='WORDLIST' ,help='Specify Your Wordlists')
	args = parser.parse_args()
	url = args.URL

	with open(args.WORDLIST) as file:
		wd=file.readlines()
	
	automate(url,wd)
def automate(url,wd):
	if requests.get(url).status_code == 200:
	 	for i in wd:
	 		directory = url+"/"+i
	 		response = requests.get(directory)
	 		if (response.status_code == 200):
	 			print("[+] 200",directory)
	 		elif (response.status_code == 403):
	 			print("[+] 403",directory)
	 		elif (response.status_code == 404):
	 			print("[+] 404",directory)
	 		elif (response.status_code == 400):
	 			print("[+] 400",directory)
	 		elif (response.status_code == 301):
	 			print("[+] 301",directory)
	 		elif (response.status_code == 302):
	 			print("[+] 302",directory)
	 		else:
	 			print("[+] NOT FOUND",directory)

	 		
	 			




if __name__ == "__main__":
	banner()
	

