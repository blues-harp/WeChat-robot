#!/usr/bin/env python
# -*- coding: utf-8 -*-
t1 = "中国"
t2 = u'[你好]'
import sys
print sys.getdefaultencoding()
# tmp.encode()
print(type(t1))
print(type(t2))
print(type(t2.encode('utf-8')))

print(t1 + t2.encode('utf-8'))
