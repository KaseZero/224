import pymysql

conn=pymysql.coonect(host="localhost",port=3306,user="root",password="root",database="p2p",charset="utf8")


coursor = conn.cursor()
coursor.execute("select * from user")
data = coursor.fetchone()

print(data)
except Exception as e:
print("错误，无法识别德德信息类型"_format(e))


finally:
