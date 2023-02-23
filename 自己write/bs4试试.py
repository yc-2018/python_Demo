# By：仰晨
# 文件名：bs4试试
# 时 间：2022/12/9 2:42
"""
    解析器	                    使用方法	                        优势
Python标准库	        BeautifulSoup(html, "html.parser")	    1、Python的内置标准库
                                                            2、执行速度适中
                                                            3、文档容错能力强
-------------------------------------------------------------------------------
lxml HTML	        BeautifulSoup(html, "lxml")	            1、速度快
                                                            2、文档容错能力强
------------------------------------------------------------------------------
lxml XML	        BeautifulSoup(html, ["lxml", "xml"])
                    BeautifulSoup(html, "xml")	            1、速度快
                                                            2、唯一支持XML的解析器
-----------------------------------------------------------------------------
html5lib	BeautifulSoup(html, "html5lib")	                1、最好的容错性
                                                            2、以浏览器的方式解析文档
                                                            3、生成HTML5格式的文档
"""

from bs4 import BeautifulSoup

# 构造一个网页数据
html_doc = """
<html>
    <head>
        <title itemprop="associatedMedia">The Dormouse's story</title>
    </head>
    <body>
        <p class="title">
            <b>The Dormouse's story</b>
            <b>ssssssssssssssssssss</b>
        </p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
        <p id="title">小黑子</p>
        <li itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
<meta itemprop="fileFormat" content="image/png">
<link itemprop="contentUrl" href="/uploads/anaconda/anaconda_PNG15.png">
<meta itemprop="keywords" content="Anaconda PNG">
<div class="png_png png_imgs">
<a itemprop="url" href="https://pngimg.com/image/54703" title="Anaconda PNG" target="_blank"><img itemprop="thumbnail" src="/uploads/anaconda/small/anaconda_PNG15.png" data-src="/uploads/anaconda/small/anaconda_PNG15.png" alt="Anaconda PNG" style="padding-top:10px;" title="Anaconda PNG" border="0" /></a>
</div>
<div class="description_div">
<div class="img_desc" itemprop="caption description"><a href="/image/54703"><b>Anaconda PNG</b></a></div>
<div class="row">
<div class="large-6 columns res_size">
Res.: 647x720 <br /> Size: 214 kb
</div>
<div class="large-6 columns">
<a href="/image/54703" class="download_png">Download</a>
</div>
</div>
</div>
</li><li itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
<meta itemprop="fileFormat" content="image/png">
<link itemprop="contentUrl" href="/uploads/anaconda/anaconda_PNG14.png">
<meta itemprop="keywords" content="Anaconda PNG">
<div class="png_png png_imgs">
<a itemprop="url" href="https://pngimg.com/image/54702" title="Anaconda PNG" target="_blank"><img itemprop="thumbnail" src="/uploads/anaconda/small/anaconda_PNG14.png" data-src="/uploads/anaconda/small/anaconda_PNG14.png" alt="Anaconda PNG" style="padding-top:10px;" title="Anaconda PNG" border="0" /></a>
</div>
<div class="description_div">
<div class="img_desc" itemprop="caption description"><a href="/image/54702"><b>Anaconda PNG</b></a></div>
<div class="row">
<div class="large-6 columns res_size">
Res.: 1000x880 <br /> Size: 852 kb
</div>
<div class="large-6 columns">
<a href="/image/54702" class="download_png">Download</a>
</div>
</div>
</div>
</li><li itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
<meta itemprop="fileFormat" content="image/png">
<link itemprop="contentUrl" href="/uploads/anaconda/anaconda_PNG13.png">
<meta itemprop="keywords" content="Anaconda PNG">
<div class="png_png png_imgs">
<a itemprop="url" href="https://pngimg.com/image/54701" title="Anaconda PNG" target="_blank"><img itemprop="thumbnail" src="/uploads/anaconda/small/anaconda_PNG13.png" data-src="/uploads/anaconda/small/anaconda_PNG13.png" alt="Anaconda PNG" style="padding-top:10px;" title="Anaconda PNG" border="0" /></a>
</div>
<div class="description_div">
<div class="img_desc" itemprop="caption description"><a href="/image/54701"><b>Anaconda PNG</b></a></div>
<div class="row">
<div class="large-6 columns res_size">
Res.: 1680x1050 <br /> Size: 1516 kb
</div>
<div class="large-6 columns">
<a href="/image/54701" class="download_png">Download</a>
</div>
</div>
</div>
</li>
    </body>
</html>
"""

# soup = BeautifulSoup("<html>A Html Text</html>", "html.parser")
# # soup.prettify()  # prettify 有括号和没括号都可以
# print(soup.prettify())
res = BeautifulSoup(html_doc, 'lxml')

print('#  获取标签----------------------------------------')
print(res.a)

print('# 获取标签内文本-------------------------------------------')
print(res.a.text)

print('# 获取标签内属性-------------------------------')
print(res.a.attrs)

print('# 获取指定属性值--------------------------------')
print(res.a.attrs.get('href'))
print(res.a.get('href'))


print('# 获取子节点------------------------------')
for i in res.p.children:
    print(i)


print('# 获取标签内部所有的元素---------------------------')
print(res.p.contents)   # 换行都算一个元素....

print('# 获取标签的父标签----------------------------')
print(res.p.parent)


print('# 获取最上级节点----------------------')
for i in res.p.parents:
    print(i)

print('上面的其实没啥用*************************************************************************')
print('# 查找指定标签名的标签 默认只找符合条件的第一个------------------')
print(res.find(name='p'))

print('# 查找具有某个特定属性的标签 默认只找符合条件的第一个----------------')
print(res.find(name='p', id='title'))

print('# 为了解决关键字冲突 会加下划线区分-------------------------')
print(res.find(name='p', class_='title'))

print('# 使用attrs参数 直接避免冲突--------------------------')
print(res.find(name='p', attrs={'class': 'title'}))


print('# 查询某一个标签，查找的结果是一个列表---**********-----*************-------***********---------')
print(res.find_all('a'))

print('# select方法---使用css选择器 该方法的返回结果是一个列表。------')
print('# 查找class含有title的标签')
print(res.select('.title'))

print('# 查看class含有sister标签内部所有的后代 b标签--------------------')
print(res.select('.title b'))

print('查找id等于title的标签------------------------------------')
print(res.select('#title'))

print('-------------------------')
print(res.find_all(name='li', attrs={'itemscope': ''}))



