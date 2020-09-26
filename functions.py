import mysql.connector
def connect_mysql(host, id, pwd, db = ""):
    try:
        mydb = mysql.connector.connect(
        host= host,
        user= id,
        password= pwd,
        database = db
        )
        mycursor = mydb.cursor()
        return(mydb)
    except Exception as ex:
        print('Error Occured : ', ex)
