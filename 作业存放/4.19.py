import pymysql

def conn():
    conn = pymysql.connect(
        host="locathost",user="root",
        password="root",db="p2p",
        port=3306,charset="utf8"
    )
    return conn

def curor(sql):
    con = conn()
    cur =con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return  result

def change_db(sql):
    con = conn()
    cur = con.cursor()
    try:
        cur.execute((sql))

        con.commit()
        execept Exeception as e:
         con.rollback()
    finally:

    result = cur.fetchall()
    return result


