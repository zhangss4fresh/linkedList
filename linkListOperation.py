# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:Zhangss
@File: linkListOperation.py
@Time:2018/01/19
"""
class Node(object):
    """
    data:节点保存的数据
    next：保存下一个节点对象
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return str(self.data)


def isEmpty(self):
    return (self.length == 0)


def arrayToList(array):
    print('The array is :%s', array1)
    head = None
    for count in range(len(array1) - 1, -1, -1):
        head = Node(array1[count], head)
    print('The Link data are:')
    while head != None:
        print(head.data)
        head = head.next


if __name__ == '__main__':
    array1 = [3, 5, 6, 0, 9]
    """ please transform array to list"""
    arrayToList(array1)
    """please add node anywhere"""
    addNode()



