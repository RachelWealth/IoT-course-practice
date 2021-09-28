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
                """create table cloth (id integer primary key,
                type varchar,
                gender varchar,
                color varchar,
                season varchar,
                brand varchar,
                create_time,
                updata_time,
                deleted integer)"""  # exist-1 deleted-0
            )
            self.cursor.execute(
                """create table flavoring (id integer primary key,
                type varchar,
                brand varchar,
                create_time,
                updata_time,
                deleted integer)""")
            self.cursor.execute(
                """create table book (id integer primary key,
                type varchar,
                author varchar,
                language varchar,
                publisher varchar,
                create_time,
                updata_time,
                deleted integer)""")
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
            a = list(row)
            id_value.append(a)
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
            a = list(row)
            id_value.append(a)
        return id_value

    def close(self):
        self.cursor.close()
        self.con.close()


"""
    以下是测试代码
"""
if __name__ == '__main__':
    db = managerSQL()
    """
    db.createTable()
    db.executeInsertcloth(1, '女', '红', '秋', 'Veromoda')
    db.executeInsertcloth(2, '女', '绿', '秋', 'Veromoda')
    db.executeInsertcloth(3, '女', '黄', '秋', 'Veromoda')
    db.executeInsertcloth(4, '女', '蓝', '夏', 'Veromoda')
    db.executeInsertcloth(5, '女', '粉', '春', 'LEDIN')
    db.executeInsertcloth(6, '女', '粉', '夏', 'LEDIN')
    db.executeInsertcloth(7, '女', '橙', '冬', 'OLNY')
    db.executeInsertcloth(8, '女', '白', '春', 'OLNY')
    db.executeInsertcloth(9, '女', '黑', '夏', 'LEDIN')
    db.executeInsertcloth(10, '女', '灰', '冬', 'OLNY')
    db.executeInsertcloth(11, '女', '红', '冬', 'OLNY')
    db.executeInsertcloth(12, '女', '绿', '春', 'LEDIN')
    db.executeInsertcloth(13, '女', '蓝', '春', 'LEDIN')
    db.executeInsertcloth(14, '女', '粉', '秋', 'LINING')
    db.executeInsertcloth(15, '女', '橙', '春', 'ANTA')
    db.executeInsertcloth(16, '女', '白', '春', 'ANTA')
    db.executeInsertcloth(17, '女', '黑', '秋', 'ANTA')
    db.executeInsertcloth(18, '女', '灰', '秋', 'ANTA')
    db.executeInsertcloth(19, '男', '红', '秋', 'SEMIR')
    db.executeInsertcloth(20, '男', '绿', '春', 'SEMIR')
    db.executeInsertcloth(21, '男', '黄', '秋', 'SEMIR')
    db.executeInsertcloth(22, '男', '蓝', '秋', 'SEMIR')
    db.executeInsertcloth(23, '男', '粉', '春', 'SEMIR')
    db.executeInsertcloth(24, '男', '橙', '春', 'ANTA')
    db.executeInsertcloth(25, '男', '白', '秋', 'Teek')
    db.executeInsertcloth(26, '男', '黑', '冬', 'Teek')
    db.executeInsertcloth(27, '男', '灰', '春', 'Teek')
    db.executeInsertcloth(28, '男', '红', '春', '特步')
    db.executeInsertcloth(29, '男', '绿', '夏', 'Teek')
    db.executeInsertcloth(30, '男', '黄', '秋', '特步')
    db.executeInsertcloth(31, '男', '蓝', '春', '特步')
    db.executeInsertcloth(32, '男', '粉', '夏', 'Teek')
    db.executeInsertcloth(33, '男', '橙', '秋', '特步')
    db.executeInsertcloth(34, '男', '白', '秋', '特步')
    db.executeInsertcloth(35, '男', '黑', '秋', '特步')
    db.executeInsertcloth(36, '男', '灰', '冬', '特步')
    db.executeInsertFlavoring(1, '海天')
    db.executeInsertFlavoring(2, '海天')
    db.executeInsertFlavoring(3, '海天')
    db.executeInsertFlavoring(4, '海天')
    db.executeInsertFlavoring(5, '海天')
    db.executeInsertFlavoring(6, '海天')
    db.executeInsertFlavoring(7, '海天')
    db.executeInsertFlavoring(8, '王守义')
    db.executeInsertFlavoring(9, '王守义')
    db.executeInsertFlavoring(10, '王守义')
    db.executeInsertFlavoring(11, '王守义')
    db.executeInsertFlavoring(12, '王守义')
    db.executeInsertBook(1, '莫言', '中文', '浙江文艺出版社')
    db.executeInsertBook(2, '莫言', '中文', '作家出版社')
    db.executeInsertBook(3, '莫言', '中文', '浙江文艺出版社')
    db.executeInsertBook(4, '鲁迅', '中文', '天津人民出版社')
    db.executeInsertBook(5, '鲁迅', '中文', '万卷出版社')
    db.executeInsertBook(6, '鲁迅', '中文', '山东画报出版社')
    db.executeInsertBook(7, '鲁迅', '中文', '中国友谊出版公司')
    db.executeInsertBook(8, '哈珀·李', '英文', 'Random UK')
    db.executeInsertBook(9, '萨默塞特·毛姆', '英文', '吉林大学出版社')
    db.executeInsertBook(10, '路易莎·梅·奥尔科特', '英文', '北京理工大学出版社')
    db.executeInsertBook(11, '弗朗西斯·霍奇森·班纳特', '英文', '北京理工大学出版社')
    db.executeInsertBook(12, '安托万·德·圣埃克苏佩里', '英文', '江苏凤凰文艺出版社')
    db.executeInsertBook(13, '东野圭吾', '中文', '南海出版社')
    db.executeInsertBook(14, '东野圭吾', '中文', '南海出版社')
    db.executeInsertBook(15, '东野圭吾', '中文', '南海出版社')

    a = db.executeQuery1('book')
    b = db.executeQuery1('cloth')
    c = db.executeQuery1('flavoring')
    print(a)
    print(b)
    print(c)
    """
    d = db.executeQuery1('cloth')
    print(d)
    #b = db.executeQuery2('book', 'author', 'liucixin')
    #db.executeUpdate('book', 2, 'publisher', '222')
    # db.executeQuery2('book',2)
    #db.executeDelete('book', 1)
    #c = db.executeQuery1('book')

    db.close()
