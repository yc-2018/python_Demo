#仰晨不牛马
#牛马时间：2022/7/9 21:06:13

"""集合间的关系
***两个集合是否相等
·可以使用运算符==或!=进行判断·一个集合是否是另一个集合的子集
·可以调用方法issubset进行判断·B是A的子集
*** —个集合是否是另一个集合的超集
·可以调用方法issuperset进行判断·A是B的超集
***两个集合是否没有交集
·可以调用方法isdisjoint进行判断
"""
print('----两个集合是否相等（排序可随意，元素要相同。==  ！=）----')

j集合a={55,22,0,13,14}
j集合b={14,13,22,0,55}

print(j集合a==j集合b)       #True
print(j集合a!=j集合b)       #False


print('------他是她的子集吗？用.issubset()')
print('------他是她的超集吗？用.issuperset()')
print('------他和她没有交集？用.isdisjoint()。有交集为false，没交集为true')

j集合c={1,2,4,5,3,0,6,7,'鸡'}
j集合d={0,1,2,3,4,5}
j集合e={'这里是','为我所统帅','的''战场',666}


print('d是c的子集吗',j集合d.issubset(j集合c))        #d是c的子集吗 True
print('c是d的子集吗',j集合c.issubset(j集合d))        #c是d的子集吗 False

print('c包涵d吗？',j集合c.issuperset(j集合d))       #c包涵d吗？ True
print('e包涵c吗？',j集合e.issuperset(j集合c))       #e包涵c吗？ False

print('c和e没有交集?',j集合c.isdisjoint(j集合e))     #c和e没有交集? True
print('d和c没有交集?',j集合d.isdisjoint(j集合c))     #d和c没有交集? False
