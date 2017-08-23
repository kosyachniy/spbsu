from func import *

alphabet='qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъёфывапролджэячсмитьбю1234567890 '

def mess(text, key):
	for i in range(len(text)):
		if text[i] not in alphabet:
			text[i]=' '
	text=text.split()

	for i in key:
		if i in text:
			return True
	return False

while True:
	with db:
		for i in  read():
			t=False
			for j in db.execute("SELECT * FROM users WHERE id=(?)", (i[0],)):
				t=True

				if j[6]:
					send(i[0], 'Расписание')

				elif j[1]=='0':
					x=''
					if mess(i[1], :
						x=''
					elif '14' in i[1]:
						x='AMCP'

					if x:
						db.execute("UPDATE users SET faculty=(?) WHERE id=(?)", (x, i[0]))
						send(i[0], 'Какая программа обучения?')
					else:
						send(i[0], 'Неверное значение 😭')

				elif j[2]==0:
					send(i[0], 'Какое направление?')
				elif j[3]==0:
					send(i[0], 'Какой год?')
				elif j[4]==0:
					send(i[0], '4')
				elif j[5]==0:
					send(i[0], '5')
				elif j[6]==0:
					#Определение
					print(j[1]+str(j[2])+str(j[3])+str(j[4])+str(j[5]))
				else:
					pass
					#Исключение с обнулением
			
			if t: continue

			db.execute("INSERT INTO users VALUES ('%d', '0', 0, 0, 0, 0, 0)" % i[0])
			send(i[0], 'Выбери факультет:\n1 - Биология\n2 - Востоковедение\n3 - Журналистика, Прикладные коммуникации\n4 - Искусства\n5 - История\n6 - Математика, Механика\n7 - Медицина\n8 - Междисциплинарные программы\n9 - Международные отношения\n10 - Международные отношения\n11 - Менеджмент\n12 - Науки о Земле\n13 - Политология\n14 - Процессы управления\n15 - Психология\n16 - Свободные искусства и науки\n17 - Социология\n18 - Стоматология и медицинские технологии\n19 - Физика\n20 - Филология\n21 - Философия\n22 - Химия\n23 - Экономика\n24 - Юриспруденция')
			#\n1 - Академическая гимназия\n7 - Колледж физической культуры и спорта, экономики и технологии