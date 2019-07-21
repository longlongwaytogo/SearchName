#!usr/bin/env python
# coding: utf-8

from enum import Enum, unique

'''
#file: main.py
#brief: main entry
#date: 2017/07/20
#author: longlongwaytogo
'''

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

@unique
class InputDataType(Enum): # 输入数据类型
    PINYIN = 0 # 使用拼音生成名字
    WORDLIB = 1 # 使用汉字词库
    ARTICLE = 2 # 使用文章进行提取，需要先获取词组，再组成名字  

print "user_setting module is import"

setting = {}

setting["name"] = "Search baby Name!" # 程序名称
setting["input_file_dir"] = "dicts/"  # 输入数据目录
setting["output_file_dir"] = "output/" # 输出数据目录


setting["pinxin"] = 0 # 0: 使用拼音作为数据
setting["mode"] = InputDataType.PINYIN # 默认使用拼音进行名字生成
setting["famliy_name"] ="" # 姓氏
setting["first_name"] ="" # 第一个名字
setting["second_name"] ="" # 第二个名字


'''
 拼音算法：
 1.基本知识：
   四声是古汉语声调的四种分类以表示音节的高低变化，包括平声、上声、去声和入声。
平声、上声、去声统称舒声，入声则为促声。舒声韵尾以元音或者鼻音结尾，促声韵尾以塞音结尾。
入声除了是一个声调，还是一系列以塞音收尾的韵母的统称。现代普通话已经失去了入声。
唐宋以来，汉语在四声的基础上区分声母清浊对应的阴调和阳调形成八声，也就是四声八调.

    四声，指古代汉语的四种声调：平、上、去、入。南北朝时，梁武帝曾经问周舍什么是“四声”，
周舍回答那就是“天（tiān）子（zǐ）圣（shèng）哲（zhé）”；这四字正好代表
“平上去入”四个不同的声调。根据日本《悉昙藏》卷五记载：“平声直低、有轻有重。上声直昂、
有轻无重。去声稍引、无轻无重。入声径止、无内无外。平中怒声、与重无别。”现代吴语中的
绍兴方言和闽南语的潮州方言区分阴阳二类声调，阴调对应清音，阳调对应浊音。

   现代汉语中的四声声调：
   拼音声调是指普通话中的声调，通常叫四声，即阴平（第一声），用“ˉ”表示，如lā；阳平第二声，
   用“ˊ”表示，如lá；上声（第三声），用“ˇ”表示，如lǎ；去声（第四声）
 对于拼音生成名字的基本思路
 1. 通过外部输入姓
 2. 通过规则进行音调匹配：如 姓4[去声] 第一个名3[上声] 第二个名2[阴平]
 3. 通过词库查找出符合这些音调的所有词语和姓氏进行过匹配
'''