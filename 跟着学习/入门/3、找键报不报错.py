# By：仰晨
# 文件名：3、找键报不报错
# 时 间：2022/11/9 1:39

dit = {'ji': '鸡', 'ni': '你', 'tai': '太', 'mei': '美'}


# 找键----------------------------------------------------------
try:
    print(dit['ji'])
    print(dit['ctrl'])
except KeyError as c:
    print(f'这种方法[不存在时]会报错{c}')                   # 这种方法[不存在时]会报错'ctrl'


print(dit.get('mei'))
print("这种方法找不到不报错，返回", dit.get('ctrl'))         # 这种方法找不到不报错，返回 None












