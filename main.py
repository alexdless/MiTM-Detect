'''
Alex Dless
MiTM Detect for gbu u-tushino
spec edit :D
'''

import sqlite3
from os import system
from re import search
from time import sleep

class Sqlite:
	def ban():
		from requests import get
		#...
		#нужны урлы в админке роутера для бана по mac'у или api microtik

	def move2ban(hw):
		from datetime import datetime
		dt = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
		conn = sqlite3.connect('database.sqlite')
		c = conn.cursor()
		if 1: #if ban():
			c.execute("INSERT INTO hws (mac, time) VALUES ('%s', '%s')" % (hw, dt))
			conn.commit()
		else:
			print("oh.. fail")
		conn.close()

	def view():
		conn = sqlite3.connect('database.sqlite')
		c = conn.cursor()
		c.execute("SELECT mac FROM hws")
		return c.fetchall()

	def clear_arp():

		if system("sudo ip neigh flush all"):
			print("arp table clear")
		else:
			print("oh.. arp table is not clear")

	def get_arp():

		system("arp -a > tmp_arp.txt")
		regexp = "(..):(..):(..):(..):(..):(..)"
		with open("tmp_arp.txt", "r") as f:
			for i in f.readlines():
				if search(regexp, i):
					result = search(regexp, i)
					if result.group() != "4c:5e:0c:bd:9e:21":
						return result.group()
		system("rm tmp_arp.txt")

while 1:
	sleep(30)
	Sqlite.move2ban(Sqlite.get_arp())
	print(Sqlite.view())
