class classifier:
    """
    collect all the value of every field to combine set
    buttons of these classfier on the right side displayed according to these set
    """

    def __init__(self):
        self.clothEN = ['color', 'brand', 'season']
        self.cloth = ['颜色', '品牌', '季节']
        self.ccolor = ['红', '绿', '黄', '蓝', '粉', '橙', '白', '黑', '灰']
        self.cbrand = ['Veromoda', 'LEDIN', 'OLNY', 'ANTA', 'SEMIR', 'Teek', '特步']
        self.cseason = ['春', '夏', '秋', '冬']

        self.flavoringEN = ['name', 'brand']
        self.flavoring = ['种类', '品牌']
        self.fname = ['盐', '味精', '鸡精', '孜然', '辣椒面', '胡椒粉']
        self.fbrand = ['海天', '王守义']

        self.bookEN = ['author', 'language', 'publisher']
        self.book = ['作者', '语言', '出版社']
        self.bauthor = ['莫言', '鲁迅', '哈珀·李', '萨默塞特·毛姆', '路易莎·梅·奥尔科特', '弗朗西斯·霍奇森·班纳特', '安托万·德·圣埃克苏佩里', '东野圭吾']
        self.blanguage = ['中文', '英文']
        self.bpublisher = ['浙江文艺出版社', '作家出版社', '天津人民出版社', '万卷出版社', '山东画报出版社', '中国友谊出版公司',
                           'Random UK', '吉林大学出版社', '北京理工大学出版社', '江苏凤凰文艺出版社', '南海出版社']

        self.homeObj = {0: 'cloth', 1: 'flavoring', 2: 'book'}
        self.home = {0: self.cloth, 1: self.flavoring, 2: self.book}
        self.homeCloth = {0: self.ccolor, 1: self.cbrand, 2: self.cseason}
        self.homeBook = {0: self.bauthor, 1: self.blanguage, 2: self.bpublisher}
        self.homeFlavoring = {0: self.fbrand}

    def addColor(self, subClass):
        self.cloth.add(subClass)

    def addbook(self, subClass):
        self.book.add(subClass)

    def addflavoring(self, subClass):
        self.flavoring.add(subClass)
