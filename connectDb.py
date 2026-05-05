import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="Recrutement_system",
        cursorclass=pymysql.cursors.DictCursor
    )