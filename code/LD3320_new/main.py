
objs = ['cloth', 'flovoring', 'book']
databases=['cloth', 'flovoring', 'book']




def findObj(objtype):
    """
    this function can search the id of object we need to find and return the retuslt
    :param objtype: type->string,
    :return: result:type->list   value:list of id we need to find
    """
    index = objs.index(objtype)
    if index ==0:
        result = queryClothDatabase()





