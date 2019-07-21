# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()

result = dag(dagparams,['wo'],120)
num = 0
for item in result:
    num = num + 1
    print(item.score, '/'.join(item.path))
    print("%d" % num)

print(20*'*')

result = dag(dagparams, ['ni', 'hao'])
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'*')

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'])
for item in result:
   # print(item.score, '/'.join(item.path))
    print(item.score,''.join(item.path))
print(20*'*')

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=2, log=True)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'*')
result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=6, log=False)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'*')

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=2, log=False)
for item in result:
    print(item.score, '/'.join(item.path))
print(20*'*')

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=1, log=False)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'=')

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shiiiii'], path_num=1, log=False)
print(result)
print(20*'=')

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', '的', 'shi'], path_num=1, log=False)
print(result)
print(20*'*')
print('\'xxx\' is unicode?', isinstance('xxx', unicode))
print('u\'xxx\' is unicode?', isinstance(u'xxx', unicode))
print( '\'xxx\' is str?', isinstance('xxx', str))
print( 'b\'xxx\' is str?', isinstance(b'xxx', str))

