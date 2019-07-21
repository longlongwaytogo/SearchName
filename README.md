# SearchName
起一个好名字

# 背景

&emsp;&emsp;宝宝已经7个月了，名字还没想好，对不程序员的准爸爸，看着各类古籍诗词，依然没有什么感觉。好吧，
&emsp;&emsp;拿出我的专长，写个程序来帮助取名吧。


# 基本思路

  &emsp;&emsp;取名字，个人认为就是从各类典籍、诗词、语录、词典中搜索出比较有内涵的字或词语。网上流行的什么五行取名、周易取名、五格取名、生成八字等不是很靠谱。 
  &emsp;&emsp;取名的目的其一是好听；其二是有给予。如果网上的各类取名，真能决定一个命运，同一天，同一刻出生，同一个名字的人，命运都一样吗。

  &emsp;&emsp;因此，决定，还是通过搜索和筛选，再加上一个音律规则来选择一些名字进行挑选。

# 程序设计思路

 1. 使用python作为开发语言。脚本语言的好处是不需要编译，同时python对网络编程有很好支持，很多爬虫程序都可以用python来实现。
 2. 程序的基本思路是： 数据输入--规则筛选--数据输出
   * 数据输入： 
   	 * 词库
   	 * 剔除词库
   * 规则筛选：
     * 单名
     * 双名
     * 字位置限制(出现在第一位，第二位，或不出现在第一位第二位）
     * 过滤名字规则
     * 
   
   * 数据输出：
     * 名字读音
     * 名字来源
     * 名字意义
     * 名字重名率

# 其他
python学习：
[廖雪峰python教程](https://www.liaoxuefeng.com/wiki/897692888725344/923056864229984)

# 第三方库

# 汉字拼音转换库：
translate chinese hanzi to pinyin by python
![xpinyin 0.5.6](https://pypi.org/project/xpinyin/)

**Install**
    pip install xpinyin

# 拼音转汉字库

![拼音转汉字， 拼音输入法引擎](https://github.com/letiantian/Pinyin2Hanzi)

  Python 2 Install：

     $ python setup.py install --user

# 汉字拼音库
![https://github.com/mozillazg/pinyin-data](https://github.com/mozillazg/pinyin-data)
