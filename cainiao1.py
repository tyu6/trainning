#!/usr/bin/env python3
#coding:utf-8
#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

num=[1,2,3,4]
i=0
for a in num:
    for b in num:
        for c in num:
            if (a!=b) and (b!=c) and (c!=a):
                i+=1
                print(a,b,c)
print('总数是: ',i)