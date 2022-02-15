# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# 以下是 filter() 方法的语法: filter(function, iterable)

def example01():
    def is_odd(n):
        return n % 2 == 1

    # 从列表中提取出奇数
    new_list = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(new_list, type(new_list))
    print(list(new_list))


def example02():
    """
    过滤出1~100中平方根是整数的数
    """
    import math
    def is_sqr(x):
        return math.sqrt(x) % 1 == 0

    new_list = filter(is_sqr, range(1, 101))
    print(new_list, type(new_list))
    print(list(new_list))


def example03():
    """
    过滤出1~100中平方根是整数的数
    """
    import math
    new_list = filter(lambda x: math.sqrt(x) % 1 == 0, range(1, 101))
    print(new_list, type(new_list))
    print(list(new_list))


if __name__ == '__main__':
    # example01()
    # example02()
    example03()
