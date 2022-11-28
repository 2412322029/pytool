#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 16:40
# @Author  : lolik
# @File    : vector.py
# @Software: PyCharm


class Vector2D:
    """
    二维坐标类 Vector2D
    实例化:  a = Vector2D(1,2) ;b = Vector2D(-3,2)
    自反:    -a = <-1,-2>
    绝对值:  abs(a) = 5**0.5
    减法:    a+b = <-2,4>
    加法:    a-b = <4,0>
    数量积 。。a*b=1
    投影     a>>b
    ...
    布尔：   only <0,0> is False
    """

    def __init__(self, x, y, **kwargs: str):
        self.x = x
        self.y = y
        if "name" in kwargs:
            self.name = kwargs["name"]
        else:
            pass

    def __str__(self) -> str:
        return f"Vector2D<{self.x},{self.y}>"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """
        平行四边形法则
        :param other: Vector2D
        :return: Vector2D
        """
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        """
        平行四边形法则
        :param other: Vector2D
        :return: Vector2D
        """
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> ("Vector2D" or int or float):
        """
        :param other: 右值为 数字 or Vector2D
        :return: Vector2D(缩放后坐标) or 数量积
        """
        if type(other) == Vector2D:
            return self.x * other.x + self.y * other.y
        elif type(other) == int or type(other) == float:
            return Vector2D(self.x * other, self.y * other)
        else:
            raise Exception(f"Vector2D不能与{other.__class__.__name__}相乘")

    def __abs__(self) -> (int or float):
        """
        |Vector2D|绝对值
        :return: 数字
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other: "Vector2D") -> bool:
        if type(other) == Vector2D:
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            raise Exception(f"Vector2D不能与{other.__class__.__name__}比较")

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.x, -self.y)

    def __rshift__(self, other: "Vector2D") -> float:
        """
        a>>b a在b上的投影
        """
        return self.__abs__() * self.vcos(other)

    def vcos(self, other: "Vector2D") -> float:
        """
        坐标夹角的余弦
        """
        __a = self.x * other.x + self.y * other.y
        __b = ((self.x ** 2 + self.y ** 2) * (other.x ** 2 + other.y ** 2)) ** 0.5
        return __a / __b


if __name__ == '__main__':
    print(Vector2D.__doc__)

    a = Vector2D(1, 2)
    b = Vector2D(2, 2)
    x = b
    c = Vector2D(2, 2)
    z = Vector2D(0, 0)

    z.x = 1
    print(-a, a * b, a * 4, a * 2.2, a * 2, a * a)

    qw = Vector2D(10, 2, name="A")
    print(qw.name)

    print(Vector2D.vcos(Vector2D(0, 1), Vector2D(0, 1)))
    print(a >> b)
