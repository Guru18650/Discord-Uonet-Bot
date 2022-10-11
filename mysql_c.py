from pickle import FALSE
import mysql.connector, discord
from datetime import date, datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sztefano"
)
mycursor = mydb.cursor()

def addHomework(name, subject, content, deadline):
  sql = "INSERT INTO homework (name, subject, content, deadline) VALUES (%s, %s, %s, %s)"
  data = datetime.strptime(deadline, '%Y-%m-%d')
  val = (name,subject,content,data)
  mycursor.execute(sql, val)
  mydb.commit()

def addExam(subject, type, topic, deadline):
  sql = "INSERT INTO exams (subject, type, topic, deadline) VALUES (%s, %s, %s, %s)"
  data = datetime.strptime(deadline, '%Y-%m-%d')
  val = (subject,type,topic,data)
  mycursor.execute(sql, val)
  mydb.commit()

def readHomework():
  sql = "SELECT * FROM homework"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  embed=discord.Embed(title="Zadania z MIGUNET+", description=date.today(), color=0x5900ff) 
  for x in myresult:
    embed.add_field(name = str(x[2])+" - " + str(x[4]), value = str(x[1]) + " - " + str(x[3]), inline=False)
  return embed
    
def readHomework():
  sql = "SELECT * FROM homework"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  embed=discord.Embed(title="Zadania z MIGUNET+", description=date.today(), color=0x5900ff) 
  for x in myresult:
    embed.add_field(name = str(x[2])+" - " + str(x[4]), value = str(x[1]) + " - " + str(x[3]), inline=False)
  return embed