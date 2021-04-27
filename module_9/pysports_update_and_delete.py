""" 
    Name:  Celeste Sila
    Date:  April 27, 2021
    Module:  9.3
    Description: Update and delete records from pysports database.
    GitHub Repository:  https://github.com/celestesila/csd-310  
"""

import mysql.connector
#from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get results  
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

# connect to pysports database 
db = mysql.connector.connect(**config) 

cursor = db.cursor()

# insert player query 
add_player = ("INSERT INTO player(first_name, last_name, team_id)"
             "VALUES(%s, %s, %s)")

# player data fields 
player_data = ("Smeagol", "Shire Folk", 1)

# insert new player record
cursor.execute(add_player, player_data)

# commit insert to database 
db.commit()

# show all records in player table 
show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

# update newly inserted record 
update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

# execute update query
cursor.execute(update_player)

# show all records in player table 
show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

# delete query 
delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

cursor.execute(delete_player)

# show all records in player table 
show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

input("\n\n  Press any key to continue... ")

db.close()