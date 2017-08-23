from func import *

while True:
	with db:
		for i in  read():
			for j in db.execute("SELECT * FROM users WHERE vkid=(?)", (i[0],)):
			send(i[0], 'Расписание')