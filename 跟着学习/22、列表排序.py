#仰晨不牛马
#牛马时间：2022/6/27 02:19:47

print('---------排序可以直接调用.sort()---------------------')

px列表=[5,4,77,168,2,8,9]     #如果不全是数字会报错TypeError: '<' not supported between instances of 'str' and 'int'

px列表.sort()                 #括号为空默认为从小到大排序#相当于括号是reverse=False
print(px列表)

px列表.sort(reverse=True)     #括号为reverse=True是从大到小排序
print(px列表)



print('---------可以调用内置函数=sorted()。会产生一个新的列表---------------------')

px列表=[44,17,21,2000,1,12]

new列表=sorted(px列表)      #默认为从小到大排序
print('原列表',px列表,'\n新列表',new列表)  #[1, 12, 17, 21, 44, 2000]

        #px列表=sorted(px列表)#不想产生新列表就=本身,不过没必要，不想产生就用sort（）就好
        #print(px列表)

new列表=sorted(px列表,reverse=True)#也可以用关键字参数变成从大到小排序
print('原列表',px列表,'\n新列表',new列表)  #[1, 12, 17, 21, 44, 2000]







