# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:Zhangss
@File: listOperate.py
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