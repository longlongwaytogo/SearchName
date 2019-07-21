#!usr/bin/python
#-*-coding:UTF-8 -*-
#python: 2.7.15
'''
#file: main.py
#brief: main entry
#date: 2017/07/20
#author: longlongwaytogo
'''
import os
import user_setting

print "Start SearchName!"

def process():
    print "Weekday.Mon:%d" % user_setting.Weekday.Mon.value
    print "process..."



if __name__ == "__main__":
    print "begin................................"
    #output_fpath = "./outputs/%s" % user_config.setting["output_fname"]
    #process(output_fpath)
    #print "user_setting name:" + user_setting.setting["name"]
    print "user_setting name:%s" % user_setting.setting["name"]
    process()
    print "over................................"
