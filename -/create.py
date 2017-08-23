import sys
sys.path.append('../')
#python3 ./-/create.py

from spbsu.func import *

with db:
	db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, faculty text, direction int, program int, year int, groups int, num int)")
	db.execute("CREATE TABLE timetable (id text PRIMARY KEY, num int)")