# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:Zhangss
@File: linkListOperation.py
@Time:2018/01/19
"""
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


if __name__ == '__main__':
    array1 = [3,5,6,0,9]
    head = None
    for count in range(len(array1)-1,-1,-1):
        head = Node(array1[count], head)
    while head != None:
        print(head.data)
        head = head.next




