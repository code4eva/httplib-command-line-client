import httplib
import sys

try:
	host_name = sys.argv[1]
except:
	host_name = "www.python.org"

conn = httplib.HTTPSConnection(host_name)
conn.request("GET", "/")

R = conn.getresponse()

if R.status != 200:
	print "Error %d making connection, status %s" %(R.status, R.reason)
else:
	data = R.read()
	conn.close()
	for item in data[:1000]:
		print item,
