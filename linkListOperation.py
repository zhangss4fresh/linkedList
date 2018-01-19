# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:Zhangss
@File: linkListOperation.py
@Time:2018/01/19
"""
class Node(object):
    """ data:节点保存的数据     next：保存下一个节点对象"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


    def __repr__(self):
        return str(self.data)


class linkList(object):
    def __init__(self):
        self.head = Node(None)
        self.length = 0


    def isEmpty(self):
        return (self.length == 0)


    # 每次在末尾添加一个节点
    def append(self, data):
        newNode = Node(data)
        pribe = self.head
        # 出现了一个愚蠢的错误，我把while循环写成if了，然后程序永远都是if，else判断一次就退出了
        while pribe.next != None:
            pribe = pribe.next
        else:
            pribe.next = newNode
            self.length += 1
        return self.length


    # 遍历整个链表
    def travel(self):
         pribe = self.head
         # 出现了一个愚蠢的错误，我把while循环写成if了，然后程序永远都是if，else判断一次就退出了
         while pribe.next != None:
             print pribe.next.data, "->"
             pribe = pribe.next
         else:
            print("None")


    # 在任意位置添加节点
    def insert(self, pos, data):
        # 首先判断要进行插入的位置是否在链表尾部
        if pos > self.length-1:
            self.append(data)
        elif pos < 0:
            self.insert(0, data)
        else:
            newNode  = Node(data)
            pribe = self.head
            count = 0
            while pribe.next != None:
                if count == pos:
                    newNode.next = pribe.next
                    pribe.next = newNode
                    self.length += 1
                    return
                else:
                    pribe = pribe.next
                    count += 1


    # 按data进行删除节点
    def remove(self, data):
        if self.isEmpty():
            return True
        else:
            pribe = self.head
            while pribe.next != None:
                if pribe.next.data == data:
                    pribe.next = pribe.next.next
                    self.length -= 1
                    return
                else:
                    pribe = pribe.next
            else:
                print "There is not the data"







if __name__ == '__main__':
    """初始化一个链表"""
    linkList1 = linkList()

    """添加节点"""
    for i in range(10):
        # print(i)
        len = linkList1.append(i)
    # python中print的写法：print "len=%d" % len      print "len=", len    print "len=" + len
    print "len = %d " %len
    linkList1.travel()

    # """ 用数组初始化链表"""
    # linkList2 = linkList()
    # array1 = [3, 5, 6, 0, 9]
    # for value in array1 :
    #     linkList2.append(value)
    # # python中print的写法：print "len=%d" % len      print "len=", len    print "len=" + len
    # linkList2.travel()

    print "按位置添加节点"
    linkList1.insert(3, 's')
    linkList1.insert(-3, "begin")
    linkList1.insert(30, "end")
    linkList1.travel()

    print "按data进行删除"
    linkList1.remove('s')
    linkList1.travel()