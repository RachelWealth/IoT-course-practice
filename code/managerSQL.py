import sqlite3
import datetime

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class managerSQL():
    def __init__(self):
        """
            初始化函数，创建数据库连接
        """
        self.con = sqlite3.connect(r"../IoT.db")
        self.cursor = self.con.cursor()

    def createTable(self):
        """
            数据库中表的创建，共三个表，分别为cloth,flavoring,book
        """
        try:
            self.cursor.execute(
                "create table cloth (id integer primary key,"
                "type varchar unique,"
                "gender varchar,"
                "color varchar,"
                "season varchar,"
                "brand varchar,"
                "create_time,"
                "updata_time,"
                "deleted integer)"  # exist-1 deleted-0
            )
            self.cursor.execute(
                "create table flavoring (id integer primary key,"
                "type varchar unique,"
                "brand varchar,"
                "create_time,"
                "updata_time,"
                "deleted integer)")
            self.cursor.execute(
                "create table book (id integer primary key,"
                "type varchar unique,"
                "author varchar,"
                "language varchar,"
                "publisher varchar,"
                "create_time,"
                "updata_time,"
                "deleted integer)")
            self.con.commit()
        except Exception as e:
            self.con.rollback()

    def executeInsertcloth(self, id, gender, color, season, brand):
        """
            数据库中cloth表的插入操作
            @:param id: 唯一标识
            @:param gender: 性别
            @:param color: 颜色
            @:param season: 季节
            @:param brand: 品牌
        """
        sql = 'insert into cloth(id,type,gender,color,season,brand,create_time,updata_time,deleted) values(?,?,?,?,?,?,?,?,?)'
        try:
            self.cursor.execute(sql, (id, "cloth", gender, color, season, brand, now_time, now_time, 0))
            self.con.commit()
        except Exception as e:
            self.con.rollback()

    def executeInsertFlavoring(self, id, brand):
        """
            数据库中flavoring表的插入操作
            @:param id: 唯一标识
            @:param brand: 品牌
        """
        sql = 'insert into flavoring(id,type,brand,create_time,updata_time,deleted) values(?,?,?,?,?,?)'
        try:
            self.cursor.execute(sql, (id, "flavoring", brand, now_time, now_time, 0))
            self.con.commit()
        except Exception as e:
            self.con.rollback()

    def executeInsertBook(self, id, author, language, publisher):
        """
            数据库中book表的插入操作
            @:param id: 唯一标识
            @:param author: 作者
            @:param language: 语言
            @:param publisher: 出版社
        """
        sql = 'insert into book(id,type,author,language,publisher,create_time,updata_time,deleted) values(?,?,?,?,?,?,?,?)'
        try:
            self.cursor.execute(sql, (id, 'book', author, language, publisher, now_time, now_time, 0))
            self.con.commit()
        except Exception as e:
            self.con.rollback()

    def executeUpdate(self, table_name, id, key, value):
        """
            数据库的修改
            @:param table_name: 需要进行更新操作的表名
            @:param id: 唯一标识，根据id进行数据库的修改
            @:param key: 需要修改的字段名
            @:param value: 更新后的值
        """
        sql = 'update ' + table_name + ' set ' + key + ' =?,updata_time=? where id=?'
        try:
            self.cursor.execute(sql, (value, now_time, id))
            self.con.commit()
        except Exception as e:
            self.con.rollback()

    def executeDelete(self, table_name, id):
        """
            数据库的删除
            @:param table_name: 需要进行删除操作的表名
            @:param id: 唯一标识，根据id进行数据库的删除
        """
        sql = 'update ' + table_name + ' set deleted =? where id=?'
        try:
            self.cursor.execute(sql, (1, id))
            self.con.commit()
        except Exception as e:
            self.con.rollback()

    def executeQuery1(self, table_name):
        """
            数据库的无条件查询
            @:param table_name: 需要进行查询操作的表名
            @:return id_value：查询结果的id数组
        """
        sql = 'select * from ' + table_name + ' where deleted=0'
        cur = self.cursor.execute(sql)
        id_value = []
        for row in cur:
            id_value.append(row[0])
        return id_value

    def executeQuery2(self, table_name, key, value):
        """
            数据库的查询
            @:param table_name: 需要进行查询操作的表名
            @:param key: 需要修改的字段名
            @:param value: 更新后的值
            @:return id_value：查询结果的id数组
        """
        sql = 'select * from ' + table_name + ' where ' + key + ' = ? and deleted=0'  # exception where deleted=1
        cur = self.cursor.execute(sql, (value,))
        id_value = []
        for row in cur:
            id_value.append(row[0])
        return id_value

    def close(self):
        self.cursor.close()
        self.con.close()


"""
    以下是测试代码
"""
if __name__ == '__main__':
    db = managerSQL()
    db.createTable()
    db.executeInsertBook(1, 'maijia', 'Chinese', 'suibian')
    db.executeInsertBook(2, 'antusheng', 'English', 'suibian')
    db.executeInsertBook(3, 'liucixin', 'Chinese', 'suibian')
    a = db.executeQuery1('book')
    b = db.executeQuery2('book', 'author', 'liucixin')
    db.executeUpdate('book', 2, 'publisher', '222')
    # db.executeQuery2('book',2)
    db.executeDelete('book', 1)
    c = db.executeQuery1('book')
    print(a)
    db.close()
