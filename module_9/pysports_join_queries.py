""" 
    Name:  Celeste Sila
    Date:  April 27, 2021
    Module:  9.2
    Description: Join Player and Team tables.
    GitHub Repository:  https://github.com/celestesila/csd-310  
"""
import mysql.connector

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# connect to pysports database 
db = mysql.connector.connect(**config) 
cursor = db.cursor()

# inner join  
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

# get results 
players = cursor.fetchall()

print("\n  -- DISPLAYING PLAYER RECORDS --")
    
# iterate over the player data set and display the results 
for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

input("\n\n  Press any key to continue... ")

db.close()