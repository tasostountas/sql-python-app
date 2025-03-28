from connection import get_connection

def view_games():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "select * FROM games"
    cursor.execute(sql)
    games = cursor.fetchall()

    if games:
        print("lista games")
        for game in games:
            print(f"Id: {game[0]}, title: {game[2]},year: {game[3]}, creator: {game[4]}, patch:{game[5]"}
    else: 
        print("den uparxoun games")
    cursor.close()
    connection.close()

view_games()