def example01():
    """
    这是一个入门示例
    """
    print("hello world！")


def example02():
    """
    获取函数的注解
    """

    class C:
        pass

    def f(a: int, b: int, c: C) -> int:
        """
        这是一个函数
        :param a: 参数1
        :param b: 参数2
        :param c: 参数3
        :return: 返回值
        """
        print(c)
        return a + b

    print(f)

    # 得到一个函数注解的字典：{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
    print(f.__annotations__)

    # 得到函数注解的类型：dict_values([<class 'int'>, <class 'int'>, <class 'int'>])
    print(f.__annotations__.values())

    # 获取函数注解的类的名称
    print("获取函数注解的类的名称")
    for item in f.__annotations__.values():
        print(item.__class__.__name__)

    print("函数的文档描述")
    print("func.__doc__: ", f.__doc__)


if __name__ == '__main__':
    # example01()
    example02()
