import sqlite3

conn = sqlite3.connect('basketball.db')
c = conn.cursor()

#c.execute('''CREATE TABLE basketball_players(
 #   player_number TEXT,
  #  player_name TEXT,
   # experience INTEGER,
    #championships INTEGER
    #)''')

#c.executemany("INSERT INTO basketball_players VALUES (?,?,?,?)", [
 #   ('23', 'LeBron James', 15, 4),
  #  ('23', 'Michael Jordan', 15, 6),
   # ('30', 'Steph Curry', 10, 3)
    #])
#c.execute("INSERT INTO basketball_players VALUES ('23', 'LeBron James', 15, 4)")
#c.execute("INSERT INTO basketball_players VALUES ('23', 'Michael Jordan', 15, 6)")
#c.execute("INSERT INTO basketball_players VALUES ('30', 'Steph Curry', 10, 3)")


#c.execute('''CREATE TABLE injuries(
 #         player_name TEXT,
  #         injury TEXT,
  #        assessment_of_cost INTEGER)''')

#c.executemany('''INSERT INTO injuries VALUES (?,?,?)''', [
 #   ('LeBron James', 'knee braked', 250),
  #  ('Michael Jordan', 'strained shoulder', 315),
   # ('Steph Curry', 'concussion', 400)
#])

c.execute("DELETE FROM basketball_players WHERE rowid NOT IN (SELECT min(rowid) FROM basketball_players GROUP BY player_name, championships, experience, player_number)")

for row in c.execute("SELECT * FROM injuries"):
    print(row)

conn.commit()
conn.close()