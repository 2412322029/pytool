#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 20:56
# @Author  : lolik
# @File    : gh.py
# @Software: PyCharm

class Side:
    def __init__(self, p1, p2, weight):
        self.p1 = p1
        self.p2 = p2
        self.weight = weight

    def __str__(self):
        return f"{self.p1}---{self.weight}---{self.p2}"

    def __repr__(self):
        return f"{self.p1}---{self.weight}---{self.p2}"


L = [
    ["A", "B", 1],
    ["A", "C", 2],
    ["B", "C", 3],
    ["B", "D", 4],
    ["D", "C", 5],
    ["D", "F", 6],
    ["C", "E", 7]
]
ls = []
for i in L:
    ls.append(Side(i[0], i[1], i[2]))
print([i for i in ls])
s = set()
for x in ls:
    s.add(x.p1)
    s.add(x.p2)
print(s)
