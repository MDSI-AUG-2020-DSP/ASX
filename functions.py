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

def mysql_list(myresult):
    try:
        db_list = [x[0].decode("utf8") for x in myresult]
    except:
        db_list = [x[0] for x in myresult]
    finally:
        return(db_list)
        