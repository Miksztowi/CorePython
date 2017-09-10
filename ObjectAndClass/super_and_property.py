# -*- encoding:utf-8 -*-
# __author__=='Gan'


class Person(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name # if return self.name, this code will lead to recursion.

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value  # if self.name = value, this code will lead to recursion.

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting Name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to ', value)
        super(SubPerson, SubPerson).name.__set__(self, value)
        # super(SubPerson, self).name.__set__(self, value) AttributeError: 'SubPerson' object has no attribute '_name'
        #  在每一个方法中，使用了 super() 来调用父类的实现。
        # 在 setter 函数中使用 super(SubPerson, SubPerson).name.__set__(self, value) 的语句是没有错的。
        # 为了委托给之前定义的setter方法，需要将控制权传递给之前定义的name属性的 __set__() 方法。
        # 不过，获取这个方法的唯一途径是使用类变量而不是实例变量来访问它。
        # 这也是为什么我们要使用 super(SubPerson, SubPerson) 的原因。

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

    #  Tips: use @Person.getter
    # class SubPerson(Person):
    #     @property  # Doesn't work
    #     @Person.getter  # work
    #     def name(self):
    #         print('Getting name')
    # >>> s = SubPerson('Guido')
    # Traceback (most recent call last):
    #     File "<stdin>", line 1, in <module>
    #     File "example.py", line 5, in __init__
    #         self.name = name
    # AttributeError: can't set attribute
    # >>>
    # 在这个特别的解决方案中，我们没办法使用更加通用的方式去替换硬编码的
    # Person
    # 类名。 如果你不知道到底是哪个基类定义了property， 那你只能通过重新定义所有property并使用
    # super()
    # 来将控制权传递给前面的实现。

if __name__ == '__main__':
    p = Person('Jasy')
    p.name = 'Jassies'

    subp = SubPerson('Nancy')
    subp.name = 'Nancies'