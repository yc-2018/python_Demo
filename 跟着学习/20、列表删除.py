#仰晨不牛马
#牛马时间：2022/6/26 02:21:51

print('----方法一---------删除列表的一个元素.remove()----------------------')

列表1=[11,22,33,44,55,22,"荔枝"]

列表1.remove(22)

print(列表1)#有多个相同元素会只删除第一个[11, 33, 44, 55, 22, '荔枝']

列表1.remove('荔枝')
print(列表1)#[11, 33, 44, 55, 22]

#列表1.remove('牛马')       #元素不存在会报异常       #ValueError: list.remove(x): x not in list



#####################################################################################################
print('----方法二---------根据索引--删除列表的一个元素.pop()----------------------')
pop列表=[00,11,22,"苏珊",'x嘻嘻']
pop列表.pop(1)        #删除索引为1的元素
print(pop列表)        #[0, 22, '苏珊', 'x嘻嘻']
pop列表.pop()         #括号为空默认删除最后一个元素
print(pop列表)        #[0, 22, '苏珊']
#pop列表.pop(9)        #索引不存在会报异常        #IndexError: pop index out of range


print('----方法三---------切片--删除列表最少一个元素[:]----------------------')
"""产生新列表"""
old列表=['零','壹','贰','叁','肆','伍']
new列表=old列表[1:4]#取1到3（不包括4）
print(old列表)
print(new列表)#['壹', '贰', '叁']
"""不产生列表"""
old列表=old列表[1:4]#对自身覆盖

old列表=['零','壹','贰','叁','肆','伍']#还原。便于举例子

old列表[1:4]=[]#把一到三的元素替换为空，剩下0、4、5
print(old列表)


print('----方法4---------清空列表.clear()----------------------')
列表=[0,1,2,3,4]
列表.clear()
#列表[0:]=[]这样切片也行
print(列表)#直接变成空列表       #[]


print('----方法5---------删除列表----------------------')
del 列表
#print(列表)  #删除就没有了，打印就会报错拉     #NameError: name '列表' is not defined












