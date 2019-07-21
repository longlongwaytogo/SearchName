#!usr/bin/python    
#-*- encoding:utf-8 -*-
print u"文件读写"

fp = open('test.txt','w+')
print u"文件名：",fp.name
print u"是否已关闭 : ",fp.closed
print u"访问模式 : ", fp.mode
print u"末尾是否强制加空格 : ", fp.softspace
fp.write("this is a test\n")
fp.writelines("this is aline test 这是一行写入测试\n")
fp.writelines("this is aline test 这是一行写入测试\n")
fp.close


