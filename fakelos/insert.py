from connection import get_connection

def insert_games (title,YEAR,genre,creator,patch):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO books() VALUES(%s, %s, %s, %s, %s)"
    Values = (title,YEAR,genre,creator,patch)
    cursor.execute(sql, Values)
    connection.commit()
    print("to game prostethike")
    cursor.close()
    connection.close()

insert_game("league of legends",2009,"moba","Steve Feak", "14.11")
insert_game("valorant",2020,"fps","David nottingham",9.11)