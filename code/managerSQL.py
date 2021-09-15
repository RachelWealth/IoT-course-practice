import sqlite3
import datetime

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
clothes=[(1,"clothe","male","red","spring","lining",now_time,now_time,0),
         (2,"clothe","male","blue","winner","bosideng",now_time,now_time,0)]
flavorings=[]
books=[]
dustbins=[]

con=sqlite3.connect(r"..\system.db")
#con.execute("create table clothe(id integer primary key,type,gender,color,season,brand,create_time,updata_time,deleted integer)")
#con.executemany("INSERT INTO clothe VALUES(?,?,?,?,?,?,?,?,?)",clothes)

con.execute("create table flavoring(id integer primary key,type,brand,create_time,updata_time,deleted integer)")
con.executemany("INSERT INTO flavoring VALUES(?,?,?,?,?,?,?,?,?)",flavorings)

con.execute("create table book(id integer primary key,type,author,language,publisher,create_time,updata_time,deleted integer)")
con.executemany("INSERT INTO book VALUES(?,?,?,?,?,?,?,?,?)",books)

con.execute("create table dustbin(id integer primary key,type,type_id)")
con.executemany("INSERT INTO book VALUES(?,?,?,?,?,?,?,?,?)",dustbins)
con.commit()

cur = con.execute("select id,gender,type,color,season,brand,create_time,updata_time,deleted from clothe")
for row in cur:   #循环输出结果
    print(row)

#以下是修改数据库字段的测试：
#con.execute("update clothe set gender=? where id=?", ('female','2'))
#con.execute("update clothe set updata_time=? where id=?", (now_time,'2'))
#con.commit()
#cur = con.execute("select id,gender,type,color,season,brand,create_time,updata_time,deleted from clothe")
#for row in cur:   #循环输出结果
#    print(row)
"""
def updataDB(id,k,v)#id为要更新字段的id，k为要更新的字段名，v为更新后的值
    cursor = db.cursor()
    try:
        update1 = "update clothe set "+k+"='"+v+"' where id="+id
        update2 = "update clothe set updata_time=now_time where id="+id
        cursor.execute(update)
        print('数据更新成功')
        db.commit()#提交数据
    except:
        print('数据更新失败')
        db.rollback()
    cursor.close()
"""
