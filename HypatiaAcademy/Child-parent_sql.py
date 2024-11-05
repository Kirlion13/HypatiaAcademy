import sqlite3
from datetime import datetime, timedelta
import random

conn = sqlite3.connect('child-parent.db')

cursor = conn.cursor()

child_table = '''CREATE TABLE IF NOT EXISTS child
    (parent_id INTEGER, child_name TEXT, date_of_birth TEXT)'''

parent_table = '''CREATE TABLE IF NOT EXISTS parent
    (parent_id INTEGER PRIMARY KEY AUTOINCREMENT, parent_name TEXT, phone INTEGER, date_of_birth TEXT)'''


cursor.execute(parent_table)

def getDate():
    from datetime import datetime, timedelta
    d = datetime.now() + timedelta(days=random.randint(-365 * 30, -365 * 18))
    return d.strftime('%Y-%m-%d')

def getNumber():
    return random.randint(1000000000, 9999999999)

def getName():
    fnames = ['John', 'Jane', 'Bob', 'Alice', 'Mark', 'Sarah', 'Emily', 'Michael', 'Jessica', 'Andrew']
    lnames = ['Smith', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas']

    return random.choice(fnames) + ' ' + random.choice(lnames)

def generate_parent_data(parent_name, phone, date_of_birth):
    parent_table_info = '''INSERT INTO parent (parent_name, phone, date_of_birth) VALUES (?, ?, ?)'''.format(parent_name, phone, date_of_birth)    
    print(parent_table_info)

    return parent_table_info


for i in range(10):
    parent_name = getName()
    phone = getNumber()
    date_of_birth = getDate()

    cursor.execute(generate_parent_data(parent_name, phone, date_of_birth))



def generate_child_data(parent_id, phone, date_of_birth, child_name):
    child_table_info = '''INSERT INTO child (parent_id, child_name, date_of_birth) VALUES (?, ?, ?)'''.format(parent_id, phone, date_of_birth, child_name)
    
    date_of_birth = getDate()
    child_name = getName()

    return child_table_info

conn.commit()

conn.close()