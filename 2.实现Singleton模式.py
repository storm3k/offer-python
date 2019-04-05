class Singleton(object):
    __instance = None
    __is_first = True

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if self.__is_first:
            self.age = age
            self.name = name
            Singleton.__is_first = False


if __name__ == '__main__':
    s = Singleton('小明', 18)
    print(s.name, s.age)
    s2 = Singleton('小王', 19)
    print(s2.name, s2.age)
    # 18 小明
    # 18 小明

