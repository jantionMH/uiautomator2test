



def assertappear(name,actual,expect):
    if actual==expect:
        print("%s成功"%name)
    else:
        print('%s失败'%name)


def asserNOTexception(name,actual,expect):
    if actual!=expect:
        print("%s异常"%name,actual)
    else:
        print('%s无异常'%name)