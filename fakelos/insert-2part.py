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

title = input("Eisagete ton titlo: ")
YEAR = int(input("Eisagete tin xronia kataskeuis: "))
genre = input("Eisagete to eidos: ")
creator = input("Eisagete ton kataskeuasti: ")
patch = input("Eisagete tin ekdosi: ")

insert_game(title,YEAR,genre,creaton,patch)