# 仰晨
# 始时间：2022/9/6 01:18:30
# 文件名：lambda


sum1 = lambda jia1, jia2: jia1 + jia2

print('50、2两个数相加', sum1(50, 2))
print('字符串可以吗？', sum1('那就', '试试吧'))

san = lambda aa, bb, cc: aa * bb * cc

print('三个数相乘', san(2, 3, 4))  # 三个数相乘 24

print('三个数相乘', san(2, '啊', 4))  # 三个数相乘 啊啊啊啊啊啊啊啊

lb = [{'id': '3333', 'name': '12', 'yy': '34', 'py': '34', 'java': '32'},
      {'id': '1000', 'name': '陈真', 'yy': '66', 'py': '77', 'java': '88'}]
a = lambda x: x[0]['name']
print(a(lb))
