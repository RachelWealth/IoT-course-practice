import sqlite3
import datetime

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class managerSQL():
    def __init__(self):
        """
            初始化函数，创建数据库连接
        """
        self.con = sqlite3.connect(r"../config/IoT.db")
        self.cursor = self.con.cursor()
        self.reBookId = 0
        self.reClothId = 0
        self.reFlaId = 0
        self.reUserId = 0

    def createTable(self):
        """
            数据库中表的创建，共四个表，分别为cloth,flavoring,book,user
        """
        try:
            self.cursor.execute(
                """create table cloth (id integer primary key autoincrement,
                type varchar,
                user varchar,
                gender varchar,
                color varchar,
                season varchar,
                brand varchar,
                create_time,
                updata_time,
                deleted integer)"""  # exist-1 deleted-0
            )
            self.cursor.execute(
                """create table flavoring (id integer primary key autoincrement,
                type varchar,
                user varchar,
                brand varchar,
                kind varchar,
                create_time,
                updata_time,
                deleted integer)""")
            self.cursor.execute(
                """create table book (id integer primary key autoincrement,
                type varchar,
                user varchar,
                author varchar,
                language varchar,
                publisher varchar,
                create_time,
                updata_time,
                deleted integer)""")
            self.cursor.execute(
                """create table user (id integer primary key autoincrement,
                name varchar,
                gender varchar,
                face_status varchar,
                password varchar,
                create_time,
                updata_time,
                deleted integer)""")
            self.con.commit()
        except Exception as e:
            self.con.rollback()

    def executeInsertcloth(self, user, gender, color, season, brand):
        """
            数据库中cloth表的插入操作
            @:param id: 唯一标识
            @:param name: 姓名
            @:param gender: 性别
            @:param color: 颜色
            @:param season: 季节
            @:param brand: 品牌
        """
        sql = 'insert into cloth(type,user,gender,color,season,brand,create_time,updata_time,deleted) values(?,?,?,?,?,?,?,?,?)'
        try:
            self.cursor.execute(sql, ("cloth", user, gender, color, season, brand, now_time, now_time, 0))
            self.con.commit()
        except Exception as e:
            self.con.rollback()
        self.reClothId = self.cursor.lastrowid
        return self.cursor.lastrowid

    def executeInsertFlavoring(self, user, kind, brand):
        """
            数据库中flavoring表的插入操作
            @:param id: 唯一标识
            @:param name: 姓名
            @:param kind: 种类
            @:param brand: 品牌
        """
        sql = 'insert into flavoring(type,user,kind,brand,create_time,updata_time,deleted) values(?,?,?,?,?,?,?)'
        try:
            self.cursor.execute(sql, ("flavoring", user, kind, brand, now_time, now_time, 0))
            self.con.commit()
        except Exception as e:
            self.con.rollback()
        self.reFlaId = self.cursor.lastrowid
        return self.cursor.lastrowid

    def executeInsertBook(self, user, author, language, publisher):
        """
            数据库中book表的插入操作
            @:param id: 唯一标识
            @:param name: 姓名
            @:param author: 作者
            @:param language: 语言
            @:param publisher: 出版社
        """
        sql = 'insert into book(type,user,author,language,publisher,create_time,updata_time,deleted) values(?,?,?,?,?,?,?,?)'
        try:
            self.cursor.execute(sql, ('book', user, author, language, publisher, now_time, now_time, 0))
            self.con.commit()
        except Exception as e:
            self.con.rollback()
        self.reBookId = self.cursor.lastrowid
        return self.cursor.lastrowid

    def executeInsertUser(self, name, password, face_status=0, gender=None):
        """
            数据库中user表的插入操作
            @:param id: 唯一标识
            @:param name: 名字
            @:param gender: 性别
            @:param username: 用户名
            @:param password: 密码
        """
        sql = 'insert into user(name,gender,username,password,create_time,updata_time,deleted) values(?,?,?,?,?,?,?)'
        try:
            self.cursor.execute(sql, (name, gender, face_status, password, now_time, now_time, 0))
            self.con.commit()
        except Exception as e:
            self.con.rollback()
        self.reUserId = self.cursor.lastrowid
        # return self.cursor.lastrowid

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

    def executeQuery(self, table_name, name=None, key=None, value=None):
        """
            数据库的无条件查询
            @:param table_name: 需要进行查询操作的表名
            @:return id_value：查询结果的id数组
        """
        cur = ''
        if (key is None) and (value is None):
            if name is not None:
                sql = 'select * from ' + table_name + ' where name = ? and deleted=0'  # exception where deleted=1
                cur = self.cursor.execute(sql, (name,))

            else:
                sql = 'select * from ' + table_name + ' where deleted=0'
                cur = self.cursor.execute(sql)
        else:
            if name is not None:
                sql = 'select * from ' + table_name + ' where name = ? and ' + key + ' = ? and deleted=0'  # exception where deleted=1
                cur = self.cursor.execute(sql, (name, value))
            else:
                sql = 'select * from ' + table_name + ' where ' + key + ' = ? and deleted=0'  # exception where deleted=1
                cur = self.cursor.execute(sql, (value,))
        des = cur.description
        id_value = []
        for row in cur:
            a = list(row)
            id_value.append(a)
        if len(id_value) != 0 and table_name == 'user':
            self.reUserId = id_value[0][0]
        return id_value, des

    # def executeQuery2(self, table_name, key, value, name=None):
    #     """
    #         数据库的查询
    #         @:param table_name: 需要进行查询操作的表名
    #         @:param key: 需要查询的字段名
    #         @:param value: 查询的值
    #         @:return id_value：查询结果的id数组
    #     """
    #     if name is not None:
    #         sql = 'select * from ' + table_name + ' where name = ? and ' + key + ' = ? and deleted=0'  # exception where deleted=1
    #     else:
    #         sql = 'select * from ' + table_name + ' where ' + key + ' = ? and deleted=0'  # exception where deleted=1
    #     cur = self.cursor.execute(sql, (value,))
    #     id_value = []
    #     des = cur.description
    #     for row in cur:
    #         a = list(row)
    #         id_value.append(a)
    #     if table_name == 'user':
    #         self.reUserId = id_value[0][0]
    #     return id_value, des

    # def executeQuery3(self, table_name, name):
    #     """
    #         对数据库根据名字进行查询
    #         @:param table_name: 需要进行查询操作的表名
    #         @:param name: 查询的名字
    #         @:return id_value：查询结果的id数组
    #     """
    #     sql = 'select * from ' + table_name + ' where name = ? and deleted=0'  # exception where deleted=1
    #     cur = self.cursor.execute(sql, (name,))
    #     id_value = []
    #     des = cur.description
    #     for row in cur:
    #         a = list(row)
    #         id_value.append(a)
    #     if table_name == 'user':
    #         self.reUserId = id_value[0][0]
    #     return id_value, des
    #
    # def executeQuery4(self, table_name, name, key, value):
    #     """
    #         在executeQuery2基础上增加名字的数据库的查询
    #         @:param table_name: 需要进行查询操作的表名
    #         @:param name: 查询的名字
    #         @:param key: 需要修改的字段名
    #         @:param value: 更新后的值
    #         @:return id_value：查询结果的id数组
    #     """
    #     sql = 'select * from ' + table_name + ' where name = ? and ' + key + ' = ? and deleted=0'  # exception where deleted=1
    #     cur = self.cursor.execute(sql, (name, value))
    #     id_value = []
    #     des = cur.description
    #     for row in cur:
    #         a = list(row)
    #         id_value.append(a)
    #     if table_name == 'user':
    #         self.reUserId = id_value[0][0]
    #     return id_value, des

    def tupleTOdic(self, cur, des):
        id_value = []
        for row in cur:
            value = {}
            for idx, col in enumerate(des):
                value[col[0]] = list(row)[idx]
            id_value.append(value)
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
    db.executeInsertUser('张三', '男', 'zhangsan', '123456')
    db.executeInsertUser('李四', '男', 'lisi', '112233')
    db.executeInsertUser('王梅', '女', 'wangmei', '111222')
    db.executeInsertUser('刘芸', '女', 'liuyun', '1234')
    db.executeInsertcloth('王梅', '女', '红', '秋', 'Veromoda')
    db.executeInsertcloth('王梅', '女', '绿', '秋', 'Veromoda')
    db.executeInsertcloth('刘芸', '女', '黄', '秋', 'Veromoda')
    db.executeInsertcloth('王梅', '女', '蓝', '夏', 'Veromoda')
    db.executeInsertcloth('刘芸', '女', '粉', '春', 'LEDIN')
    db.executeInsertcloth('刘芸', '女', '粉', '夏', 'LEDIN')
    db.executeInsertcloth('王梅', '女', '橙', '冬', 'OLNY')
    db.executeInsertcloth('王梅', '女', '白', '春', 'OLNY')
    db.executeInsertcloth('刘芸', '女', '黑', '夏', 'LEDIN')
    db.executeInsertcloth('王梅', '女', '灰', '冬', 'OLNY')
    db.executeInsertcloth('王梅', '女', '红', '冬', 'OLNY')
    db.executeInsertcloth('刘芸', '女', '绿', '春', 'LEDIN')
    db.executeInsertcloth('刘芸', '女', '蓝', '春', 'LEDIN')
    db.executeInsertcloth('王梅', '女', '粉', '秋', 'LINING')
    db.executeInsertcloth('王梅', '女', '橙', '春', 'ANTA')
    db.executeInsertcloth('刘芸', '女', '白', '春', 'ANTA')
    db.executeInsertcloth('刘芸', '女', '黑', '秋', 'ANTA')
    db.executeInsertcloth('刘芸', '女', '灰', '秋', 'ANTA')
    db.executeInsertcloth('张三', '男', '红', '秋', 'SEMIR')
    db.executeInsertcloth('张三', '男', '绿', '春', 'SEMIR')
    db.executeInsertcloth('李四', '男', '黄', '秋', 'SEMIR')
    db.executeInsertcloth('张三', '男', '蓝', '秋', 'SEMIR')
    db.executeInsertcloth('李四', '男', '粉', '春', 'SEMIR')
    db.executeInsertcloth('李四', '男', '橙', '春', 'ANTA')
    db.executeInsertcloth('李四', '男', '白', '秋', 'Teek')
    db.executeInsertcloth('张三', '男', '黑', '冬', 'Teek')
    db.executeInsertcloth('李四', '男', '灰', '春', 'Teek')
    db.executeInsertcloth('李四', '男', '红', '春', '特步')
    db.executeInsertcloth('张三', '男', '绿', '夏', 'Teek')
    db.executeInsertcloth('张三', '男', '黄', '秋', '特步')
    db.executeInsertcloth('张三', '男', '蓝', '春', '特步')
    db.executeInsertcloth('李四', '男', '粉', '夏', 'Teek')
    db.executeInsertcloth('李四', '男', '橙', '秋', '特步')
    db.executeInsertcloth('张三', '男', '白', '秋', '特步')
    db.executeInsertcloth('李四', '男', '黑', '秋', '特步')
    db.executeInsertcloth('李四', '男', '灰', '冬', '特步')
    db.executeInsertFlavoring('李四', '酱油', '海天')
    db.executeInsertFlavoring('张三', '酱油', '海天')
    db.executeInsertFlavoring('刘芸', '酱油', '千禾')
    db.executeInsertFlavoring('王梅', '酱油', '海天')
    db.executeInsertFlavoring('李四', '味精', '太太乐')
    db.executeInsertFlavoring('王梅', '酱油', '海天')
    db.executeInsertFlavoring('张三', '酱油', '海天')
    db.executeInsertFlavoring('王梅', '味精', '莲花')
    db.executeInsertFlavoring('李四', '味精', '国莎')
    db.executeInsertFlavoring('刘芸', '食盐', '中盐')
    db.executeInsertFlavoring('李四', '食盐', '双晶')
    db.executeInsertFlavoring('刘芸', '食盐', '淮盐')
    db.executeInsertFlavoring('刘芸', '食盐', '淮盐')
    db.executeInsertBook('王梅', '莫言', '中文', '浙江文艺出版社')
    db.executeInsertBook('刘芸', '莫言', '中文', '作家出版社')
    db.executeInsertBook('张三', '莫言', '中文', '浙江文艺出版社')
    db.executeInsertBook('王梅', '鲁迅', '中文', '天津人民出版社')
    db.executeInsertBook('刘芸', '鲁迅', '中文', '万卷出版社')
    db.executeInsertBook('刘芸', '鲁迅', '中文', '山东画报出版社')
    db.executeInsertBook('张三', '鲁迅', '中文', '中国友谊出版公司')
    db.executeInsertBook('张三', '哈珀·李', '英文', 'Random UK')
    db.executeInsertBook('王梅', '萨默塞特·毛姆', '英文', '吉林大学出版社')
    db.executeInsertBook('张三', '路易莎·梅·奥尔科特', '英文', '北京理工大学出版社')
    db.executeInsertBook('刘芸', '弗朗西斯·霍奇森·班纳特', '英文', '北京理工大学出版社')
    db.executeInsertBook('张三', '安托万·德·圣埃克苏佩里', '英文', '江苏凤凰文艺出版社')
    db.executeInsertBook('李四', '东野圭吾', '中文', '南海出版社')
    db.executeInsertBook('李四', '东野圭吾', '中文', '南海出版社')
    db.executeInsertBook('王梅', '东野圭吾', '中文', '南海出版社')
"""
    # a = db.executeQuery1('book')
    # b = db.executeQuery1('cloth')
    # c = db.executeQuery1('flavoring')
    # # d = db.executeQuery1('user')
    # e = db.executeQuery4('cloth', '张三', 'color', '蓝')
    # print(a)
    # print(b)
    # print(c)
    # print(e)
    """
    d, des = db.executeQuery1('cloth')
    print(d)
    dd = db.tupleTOdic(d, des)
    print('cloth dic----------------------------------\n\n\n\n')
    print(dd)
    print('----------------------------------\n\n\n\n')
    b = db.executeQuery2('book', 'author', 'liucixin')
    print(b)
    # db.executeUpdate('book', 2, 'publisher', '222')
    # db.executeQuery2('book',2)安托万·德·圣埃克苏佩里
    # db.executeDelete('book', 1)
    # c = db.executeQuery1('book')
    """
    a = db.executeQuery(table_name='user', key='name', value='刘芸')

    db.close()
