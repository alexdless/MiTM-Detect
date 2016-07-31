'''
Alex Dless
MiTM Detect for gbu u-tushino
spec edit :D
'''

from sh import arp
import sqlite3

class Sqlite:
	def ban():
		from requests import get
		#...
		#нужны урлы в админке роутера для бана по mac'у

	def move2ban(hw):
		from datetime import datetime
		dt = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
		conn = sqlite3.connect('database.sqlite')
		c = conn.cursor()
		if 1: #if ban():
			c.execute("INSERT INTO hws (banned) VALUES ('%s %s')" % (hw, dt))
			conn.commit()
		else:
			print("oh.. fail")
		conn.close()

	def view():
		conn = sqlite3.connect('database.sqlite')
		c = conn.cursor()
		c.execute("SELECT banned FROM hws")
		return c.fetchall()

	def clear_arp():
		from os import system
		if system("sudo ip neigh flush all"):
			print("arp table clear")
		else:
			pprint("oh.. arp table is not clear")


#print(Sqlite.view())
Sqlite.move2ban("192.168.1.11")
print(Sqlite.view())