# By：仰晨
# 文件名：正则替换
# 时 间：2023/2/28 2:42
import re

sample_string = 'Th\nis/is\\a?sample*string:with|special"characters<>.'
sanitized_string = re.sub(r'[/\\?*:|\n"<>]', ' ', sample_string)
print(sanitized_string)
