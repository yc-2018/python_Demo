import re

规则 = r"(?<=href=\")(/video.+?)(?=\")"

txt = """href="/video/6975745672439926019" class href="/video/697aaaa439926019"="B3A href="/video/69757456aa2439926019"sd"""


end = re.findall(规则, txt)       # findall 可以返回多个，   re.search()就一个

print(end)                              # ['/video/6975745672439926019', '/video/697aaaa439926019', '/video/69757456aa2439926019']
print('--------------------')
print(re.findall(规则, txt))