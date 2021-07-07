import mysql.connector
import datetime

def convertToBinaryData(filename):
    with open(filename,'rb') as file:
        binaryData=file.read()
    return binaryData
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="covid"
)
mycursor=mydb.cursor()
image=convertToBinaryData('image.jpg')
datetime_object = datetime.datetime.now()

def sqlupload(name,number,temp):
    sql = "INSERT INTO suspect (name,number,image,temperature,time_date) VALUES (%s, %s, %s, %s, %s)"
    val = (name,number,image,temp,datetime_object)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")