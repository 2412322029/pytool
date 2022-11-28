#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 19:55
# @Author  : lolik
# @File    : line.py
# @Software: PyCharm

from vector import Vector2D as V2
from fractions import Fraction


class Line:
    # y=ax+b
    missing_range = 0.0001  # 精度

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __contains__(self, item: V2) -> bool:
        if abs(self.a * item.x + self.b - item.y) < self.missing_range:
            return True
        else:
            return False

    def __str__(self):
        return f"y = {self.a}x + {self.b}"

    @staticmethod
    def twopoint(p1: V2, p2: V2):
        a = Fraction((p1.y - p2.y) / (p1.x - p2.x))
        b = p1.y - a * p1.x
        return Line(a, b)


x = Line(1, 0)
A = V2(2, -2)

print(A in x)

B = V2(1.22, 1.1)
L1 = Line.twopoint(A, B)
print(L1, x, L1.a)
print(B in L1, A in L1)
