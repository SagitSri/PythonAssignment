import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'flaskdb',
  'raise_on_warnings': True
}


def checkUserExists(mailId,psw):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    print(cursor.execute("SELECT * FROM user where user_mail=%s and user_psw=%s", (mailId,psw)))
    records = cursor.fetchall()
    print(records)
    cursor.close()
    cnx.close()
    return True if records else False

def addUser(userfname, userlname, userdob, usermail, userpassword):
    cnx = mysql.connector.connect(**config)
    add_user_query = ("INSERT INTO user (user_name, user_dob, user_mail, user_psw) "
  "VALUES (%s, %s, %s, %s)")
    cursor = cnx.cursor(buffered=True)
    print(add_user_query)
    cursor.execute(add_user_query,((userfname+userlname), userdob, usermail, userpassword))
    cnx.commit()
    cursor.close()
    cnx.close()
        
