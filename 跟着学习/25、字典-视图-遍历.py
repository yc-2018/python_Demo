#仰晨不牛马
#牛马时间：2022/7/3 03:46:37

z字典={'鸡':'ji','你':'ni','太':'tai','美':'mei',"牛避":666}

print('------------------------获取字典的所有键.keys()------------------------------------')

j键=z字典.keys()       #获取字典的所有键key

j变列表=list(j键)       #把获取的键赋值变成一个列表
print(j键,type(j键))           #dict_keys(['鸡', '你', '太', '美', '牛避']) <class 'dict_keys'>
print(j变列表,type(j变列表))    #['鸡', '你', '太', '美', '牛避'] <class 'list'>

print('------------------------获取字典的所有值.values()------------------------------------')
v值=z字典.values()         #获取字典的所有值value
print(v值,type(v值))      #dict_values(['ji', 'ni', 'tai', 'mei', 666]) <class 'dict_values'>
print(list(v值))         #转换为列表输出    #['ji', 'ni', 'tai', 'mei', 666]

print('------------------------获取字典的所有键值对items()------------------------------------')
i键值对=z字典.items()        #获取字典的所有键值对

print(i键值对)
        #dict_items([('鸡', 'ji'), ('你', 'ni'), ('太', 'tai'), ('美', 'mei'), ('牛避', 666)])
print(type(i键值对))       #<class 'dict_items'>
print(list(i键值对))       #键值对转列表会变成元组组成（下章才学到，先了解有这个东西）
        #[('鸡', 'ji'), ('你', 'ni'), ('太', 'tai'), ('美', 'mei'), ('牛避', 666)]



print('###########################---字典的遍历---#############################################')

z遍历字典={'鸡':'ji','你':'ni','太':'tai','美':'mei',"牛避":666}

for i增量 in z遍历字典:
    print(i增量,end='')   #鸡你太美牛避  #遍历会拿到字典的key键
    print(z遍历字典[i增量],'或者',z遍历字典.get(i增量))   #鸡ji 或者 ji      #这样就可以获取字典的值
                                                    #你ni 或者 ni
                                                    #太tai 或者 tai
                                                    #美mei 或者 mei
                                                    #牛避666 或者 666






