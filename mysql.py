#!/usr/bin/env python
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import datetime

def Get():
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password= "123456",
    database="outputs",
    charset="utf8")
 
 
    cursor = conn.cursor() 
    sql = "select output from  outputs order by id"
 
    cursor.execute(sql)
    mresults = cursor.fetchall()
    for x in mresults:
        y = x[0]
        y = y.replace("\r\n", " ")
        y = y.replace("\n", " ")
        print y
    cursor.close()
    conn.close()
    return 

def GetId(wid):
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password= "123456",
    database="outputs",
    charset="utf8")
 
 
    cursor = conn.cursor() 
    sql = "select output from  outputs where id = %s"%(wid)
 
    cursor.execute(sql)
    mresults = cursor.fetchall()
    for x in mresults:
        print x[0]
    cursor.close()
    conn.close()
    return 


if __name__ == "__main__":
    results = Get()
    #print GetId(9000)
