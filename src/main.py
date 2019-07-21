#!usr/bin/env python
#-*-coding:UTF-8 -*-
#python: 2.7.15
from __future__ import (print_function,unicode_literals)

'''
#file: main.py
#brief: main entry
#date: 2017/07/20
#author: longlongwaytogo
'''

import os
import user_setting
from user_setting import setting
import pinyin # 拼音处理流程




print("Start SearchName!")

def process():
    print("start process...")
    if setting["mode"] == user_setting.InputDataType.PINYIN:
        print ("Mode is:{0}".format(user_setting.InputDataType.PINYIN))
        pinyin.main()

    elif setting["mode"] == user_setting.InputDataType.WORDLIB:
        print("Mode is:{0}".format(user_setting.InputDataType.WORDLIB))
    
    elif setting["mode"] == user_setting.InputDataType.ARTICLE:
        print("Mode is:{0}".format(user_setting.InputDataType.ARTICLE))
    print ("end process...")




if __name__ == "__main__":
    print ("begin................................")
    #output_fpath = "./outputs/%s" % user_config.setting["output_fname"]
    #process(output_fpath)
    #print "user_setting name:" + user_setting.setting["name"]
    print("user_setting name:%s" % user_setting.setting["name"])
    process()
    print("over................................")
