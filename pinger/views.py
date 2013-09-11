
from django.http import HttpResponse
from django.shortcuts import render
import threading
import httplib
from time import sleep

class WaitAndCallThread(threading.Thread):
	def __init__(self,urls):
		threading.Thread.__init__(self)
		self.urls = urls

	def run(self):
		# after 45 minutes.
		sleep(2700)
		for url in self.urls:
			conn = httplib.HTTPConnection(url)
			conn.request("GET", "/")
			res = conn.getresponse()
			print url, res.status, res.reason
		print "done with wake up call"

def home(request):
	urls = ["www.cmu-jsa.com", "www.webtext.me"]
	thread = WaitAndCallThread(urls)
	thread.start()
 	return HttpResponse("hello pinger")


