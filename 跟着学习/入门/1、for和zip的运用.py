# By：仰晨
# 文件名：for和zip的运用
# 时 间：2022/11/9 0:52

# 把两个序列打包组合

lst = ['鸡', '你', '太', '美']

tup = '只因', '伱', '钛', '镁', '了'

dit = {}

for ls, tu in zip(lst, tup):        # 循环取短的
    print(ls, tu)

    '''
    运行结果：
    鸡 只因
    你 伱
    太 钛
    美 镁
    '''
    dit[ls] = tu

print(dit)      # {'鸡': '只因', '你': '伱', '太': '钛', '美': '镁'}

print([list(z) for z in zip(lst, tup)])







