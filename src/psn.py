import time
import notify2
import cookielib
import urllib
import urllib2
import os


cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

urllib2.install_opener(opener)

authentication_url = 'http://puzzlepedia.esy.es/adminlogin.php'

payload = {
  'lemail': 'AdminEmail',
  'lpwd': 'AdminPassword'
  }

data = urllib.urlencode(payload)

req = urllib2.Request(authentication_url, data)

resp = urllib2.urlopen(req)
contents = resp.read()

url=urllib2.urlopen("http://puzzlepedia.esy.es/evaluate.php")
s = url.read()


while 'submission' in s:
	# path to notification window icon
	ICON_PATH = "/home/rahul/Downloads/PSC/src/notify.png"
	 
	 
	# initialise the d-bus connection
	notify2.init("Pending Submission Notifier")
	 
	# create Notification object
	n = notify2.Notification(None, icon = ICON_PATH)
	 
	# set urgency level
	n.set_urgency(notify2.URGENCY_NORMAL)
	 
	# set timeout for a notification
	n.set_timeout(10000)
	 
	# update notification data for Notification object
	n.update("Puzzlepedia","Submission Checking Pending")
	 
	# show notification on screen
	n.show()
	
	a=300
	b=2000

	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( a, b))

	# short delay between notifications
	time.sleep(15)


