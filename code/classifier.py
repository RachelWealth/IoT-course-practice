from managerSQL import managerSQL


class classifier:
    """
    collect all the value of every field to combine set
    buttons of these classfier on the right side displayed according to these set
    """

    def __init__(self):
        self.cloth = {'颜色', '品牌', '季节'}
        self.ccolor = {'红色', '绿色', '黄色', '蓝色', '粉色', '橙色', '白色', '黑色', '灰色'}
        self.cbrand = {'夏奈尔', '路易·威登', '迪奥'}
        self.cseason = {'春装', '夏装', '秋装', '冬装'}

        self.flavoring = {'盐', '味精', '鸡精', '孜然', '辣椒面', '胡椒粉'}
        self.fbrand = {'味好美', '太太乐'}

        self.book = {'作者', '语言', '出版社'}
        self.bauthor = {'狄金森', '宗璞', '简·奥斯丁'}
        self.blanguage = {'中文', '英文'}
        self.bpublisher = {'人民出版社', '机械出版社'}

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