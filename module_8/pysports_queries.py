""" 
    Name:  Celeste Sila
    Date:  April 21, 2021
    Module:  8.2
    Title: PySports: Table Queries
    Description: Query MySQL database  
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    # connect to pysports database 
    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    # query team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # get results 
    teams = cursor.fetchall()

    # print teams label
    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # iterate over teams data set and display results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # query player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get the results 
    players = cursor.fetchall()

    # print player label
    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # iterate over players data set and display results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

# error handling
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    # close connection to MySQL    
    db.close()