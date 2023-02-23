# By：仰晨
# 文件名：Pyecharts实现数据可视化
# 时 间：2022/12/12 14:32
"""老师给的test4.xlsx只有count一列     自己改成countA和countB 两列"""
import time
import json
import pandas as pd
import numpy as np
import re
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar, Map, Line, Page, Pie, Funnel, Gauge, WordCloud, Geo

# %matplotlib inline

# 1制简单柱状图1111111111
"""
data = pd.read_excel("./data/test4.xlsx")
# print(data.head())
xdata = data['typename']
ydata = data['countA']
bar = (Bar().add_xaxis(xdata.tolist())
        .add_yaxis("销售数量", ydata.tolist())
        .set_global_opts(title_opts=opts.TitleOpts(title="某商场A商家商品销售数量情况")))
# bar.render_notebook()
# 自行创建文件夹new_data
bar.render(path="./new_data/1、销售数量.HTML")            # 生成html
"""

# 2.绘制动态控制柱状图222222222222222222
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename']
yAdata = data['countA']
yBdata = data['countB']
bar = (Bar().add_xaxis(xdata.tolist())
       .add_yaxis("A商家销售数量", yAdata.tolist())
       .add_yaxis("B商家销售数量", yBdata.tolist())
       # 图形标题设置
       .set_global_opts(title_opts=opts.TitleOpts(title="某商场商家商品销售数量对比",
                                                  pos_left="center",
                                                  pos_top="7%"),
                        tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis',
                                                      axis_pointer_type='shadow'),  # 'shadow':阴影指示器
                        # 图例的设置
                        legend_opts=opts.LegendOpts(pos_top='12%', pos_left='45%'),
                        # 视觉映射配管项
                        visualmap_opts=opts.VisualMapOpts(type_='color',
                                                          min_=np.min(yAdata),
                                                          max_=np.max(yAdata),
                                                          range_text=['High', 'Low'], ),
                        # x轴坐标配置项
                        xaxis_opts=opts.AxisOpts(name='商品类别',
                                                 axislabel_opts={'interval': '0'}),
                        # y轴配置项
                        yaxis_opts=opts.AxisOpts(name='数量',
                                                 min_=0,
                                                 type_='value',
                                                 axislabel_opts=opts.LabelOpts(formatter='{value}'), ),
                        # 区城缩放配管项
                        datazoom_opts=opts.DataZoomOpts(range_start=5, range_end=50), ))
bar.render(path="./new_data/2、销售数量对比.HTML")  # 生成html
"""

# 3利用bar,reversal_axis()绘制水平的直方图333333333333333333333333333333333333
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename']
yAdata = data['countA']
yBdata = data['countB']
bar = Bar()
bar.add_xaxis(xdata.tolist())
bar.add_yaxis('商家A', yAdata.tolist())
bar.add_yaxis('商家B', yBdata.tolist())
bar.set_global_opts(title_opts=opts.TitleOpts(title='货品销售情况', subtitle="A和B公司"),
                    toolbox_opts=opts.ToolboxOpts(is_show=True))
bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
bar.reversal_axis()
bar.render(path="./new_data/3、销售数量对比.HTML")  # 生成html
"""

# 4.绘制堆叠图44444444444444444444444444444
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename']
yAdata = data['countA']
yBdata = data['countB']
bar = Bar()
stack_bar = (Bar(init_opts=opts.InitOpts(width='900px', height='500px'))
             .add_xaxis(xdata.tolist())
             .add_yaxis("商家A", yAdata.tolist(), stack='stackl')
             .add_yaxis("商家B", yBdata.tolist(), stack='stackl')
             .set_global_opts(title_opts=opts.TitleOpts(title='堆叠图'))
             .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
             )
stack_bar.render(path="./new_data/4、销售数量对比堆叠图.HTML")  # 生成html
"""

# 5 饼图55555555555555555555555555555555555555555555555
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename']
p = round(data['countA']/data['countA'].sum()*100, 2)
c = Pie()
c.add("", [list(z) for z in zip(xdata, p)])
c.set_global_opts(title_opts=opts.TitleOpts(title='商家A的各类商品销售数量占比'))
c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
c.render(path="./new_data/5、销售数量对比饼图.HTML")  # 生成html
"""

# 6.环形饼图:通过参教圆形饼图radius可以条制环形饼图
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename']
p = round(data['countA']/data['countA'].sum()*100, 2)
c = Pie()
c.add("销售量占比", [list(z) for z in zip(xdata, p)], radius=[80, 150])
c.set_global_opts(title_opts=opts.TitleOpts(title='商家A的各类商品销售数量占比'))
c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
c.render(path="./new_data/6、销售数量对比环形饼图.HTML")  # 生成html
"""

# 7.玫瑰图绘制
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename']
p = round(data['countA']/data['countA'].sum()*100, 2)
c = Pie(init_opts=opts.InitOpts(width='900px', height='600px', bg_color='white'))
c.add("销售量占比", [list(z) for z in zip(xdata, p)], radius=['20%', '70%'], center=['40%', '60%'], rosetype='radius')
c.set_global_opts(title_opts=opts.TitleOpts(title='商家A的各类商品销售数量占比'))
c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
c.render(path="./new_data/7、销售数量对比玫瑰图.HTML")  # 生成html
"""

# 8漏斗图
"""
data = pd.read_excel("./data/test4.xlsx")
data.sort_values(by=['countA'], ascending=False, inplace=True)  # 对这行降序排序 原表进行
labels = data['typename']
wf = Funnel()
wf.add('商家A的商品销量情况', [list(z) for z in zip(labels, data['countA'])], is_selected=True)
wf.render(path="./new_data/8、销售数量A漏斗图.HTML")  # 生成html
"""

# 9仪表盘图---------------
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename']
p = round((data['countA']*data['price']).sum()/(data['money'].sum())*100, 2)
c = Gauge()
c.add('业务指标', [('完成率', p)], axisline_opts=opts.AxisLineOpts(
    linestyle_opts=opts.LineStyleOpts(color=[(0.3, '#67e0e3'), (0.7, '#37a2da'), (1, '#fd666d')], width=30)))
c.set_global_opts(title_opts=opts.TitleOpts(title='商家A的营业完成率'), legend_opts=opts.LegendOpts(is_show=False))
c.render(path="./new_data/9、商家A的营业完成率 仪表盘图.HTML")  # 生成html

"""

# 10.折线趋势图1
"""
gdp_data = pd.read_csv('data/provinces_gdp.csv', encoding='GB2312')  # pandas读Acsv表
pop_data = pd.read_csv('data/provinces_population.csv', encoding='GB2312')
attr = gdp_data.columns.tolist()[-1:0:-1]  # 年份
province = "广东省"
v1 = gdp_data[gdp_data['地区'] == province].values.tolist()[0][-1:0:-1]  # 历年CDP数据
v2 = pop_data[pop_data['地区'] == province].values.tolist()[0][-1:0:-1]  # 历年人口教指
line = (Line().add_xaxis(xaxis_data=attr)
        .add_yaxis(series_name="GDP数据", y_axis=v1, is_smooth=True)
        .add_yaxis(series_name="人口数据", y_axis=v2, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title='历年GDP与人口变化曲线')))

line.render(path="./new_data/10、历年GDP与人口变化曲线趋势图.HTML")  # 生成html/
"""

# 11.折线趋势图2
"""
gdp_data = pd.read_csv('data/provinces_gdp.csv', encoding='GB2312')  # pandas读Acsv表
pop_data = pd.read_csv('data/provinces_population.csv', encoding='GB2312')
attr = gdp_data.columns.tolist()[-1:0:-1]  # 年份
province = "广东省"
v1 = gdp_data[gdp_data['地区'] == province].values.tolist()[0][-1:0:-1]  # 历年CDP数据
v2 = pop_data[pop_data['地区'] == province].values.tolist()[0][-1:0:-1]  # 历年人口教指
line = (Line().add_xaxis(xaxis_data=attr)
        .add_yaxis(series_name="GDP数据", y_axis=v1, is_smooth=True, symbol_size=7, symbol='triangle',
                   linestyle_opts=opts.LineStyleOpts(width=3, type_='dotted', color='#7e9af1'))
        .add_yaxis(series_name="人口数据", y_axis=v2, is_smooth=True, symbol_size=6,
                   linestyle_opts=opts.LineStyleOpts(width=3, type_='dotted', color='#6f9ef1'))
        .set_global_opts(title_opts=opts.TitleOpts(title='历年GDP与人口变化曲线'),
                         datazoom_opts=opts.DataZoomOpts(range_start=5, range_end=50)))
line.render(path="./new_data/11、历年GDP与人口变化曲线趋势图2.HTML")  # 生成html
"""

# 12.条制混合图，折线图和柱形图混合
"""
data = pd.read_excel("./data/test4.xlsx")
xdata = data['typename'].tolist()
yAdata = data['countA'].tolist()
yBdata = data['countB'].tolist()
bar = Bar()
bar.add_xaxis(xdata)
bar.add_yaxis('商家A', yAdata, label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('商家B', yBdata, label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(title_opts=opts.TitleOpts(title='混合图'),
                    tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross'),
                    xaxis_opts=opts.AxisOpts(type_='category', axispointer_opts=opts.AxisPointerOpts(is_show=True,
                                                                                                     type_='shadow')))
bar.extend_axis(yaxis=opts.AxisOpts(name='销量', min_=0, max_=1000))
line = (Line()
        .add_xaxis(xdata)
        .add_yaxis('商家A的销量', yAdata, is_selected=True, symbol_size=7)
        .add_yaxis('商家B的销量', yBdata, is_selected=True, symbol_size=6,
                   linestyle_opts=opts.LineStyleOpts(width=3, type_='dotted', color='#6f9ef1')))

bar.overlap(line)   # 合并图
line.render(path="./new_data/12、商家的销量对比混合图.HTML")  # 生成html
"""

# 13.内宣简单形状词云路
"""
'''WordCloud.add0方法简介##############
add(name, attr,value,
    shape= 'circle'
    word_gap=20,
    word_size_range=None,
    rotate_step=45)
    
    name str 图例名称
    attr list 属性名称
    value list 属性所对应的值
    shape 词云图轮廓 对应属性可选 'circle’，'rect','roundRect', 'triangle', 'diamond', 'pin','arrow'
    word_gap int 字符间隔认为20
    word_size_range 字符范围黑认为[12,60]
    rotate_step int 旋转角度认为45
#######################################'''

data = pd.read_excel("./data/test4.xlsx", sheet_name=1)
wordcloud_data = data.to_records(index=False).tolist()
wc = WordCloud()
wc.add("", wordcloud_data, word_size_range=[15, 30], shape='diamond', word_gap=60)
wc.set_global_opts(title_opts=opts.TitleOpts(title='词云关键字展示'))
wc.render(path="./new_data/13、词云关键字展示.HTML")  # 生成html
"""

# 14.自定义形状词云图
"""
data = pd.read_excel("./data/test4.xlsx", sheet_name=1)
wordcloud_data = data.to_records(index=False).tolist()
wc = WordCloud()
wc.add("热点技术", wordcloud_data, word_size_range=[15, 30], word_gap=60, mask_image='./data/cat.png')
wc.set_global_opts(title_opts=opts.TitleOpts(title='热点技术词云图'))
wc.render(path="./new_data/14、自定义形状词云图.HTML")  # 生成html
"""

# 15中国国家地图，近20年全国各省CDP增长率地图
"""
gdp_data = pd.read_csv('data/provinces_gdp.csv', encoding='GB2312')
_attr = gdp_data['地区'].values.tolist()  # 省份
arrt = [re.sub('[自治区市省回族维吾尔壮]', '', i) for i in _attr]
value = []

for i in _attr:
    gdp = gdp_data[gdp_data['地区'] == i].values.tolist()[0][-1:0:-1]  # 历年GDP数据
    rate = round(gdp[-1] / gdp[0], 2)
    value.append(rate)
map1 = (
    Map().add('增长率/倍', [list(z) for z in zip(arrt, value)], "china", is_map_symbol_show=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="全国各省GDP增长率地图"),
                     visualmap_opts=opts.VisualMapOpts(max_=20)))
# 用额色图例表示数据特征，连续性表示，max 表示图例展示的大数值，如果比该数值大，那么颜色都是一样的
map1.render(path="./new_data/15、中国国家地图.HTML")  # 生成html
"""

# 16.世界地图，2022年06月13日世界新冠死亡人数可视化
"""
data = pd.read_csv('data/today_worlds_2022_06_13.csv')
data.fillna(0)  # 空值填充
# 由于世界地图的国家名默认为英文，所以如果爬取的国家名是中文则可视化后不显示数据，需要将中文名转换为英文名
# 设置世界地图的大小，否则图上的文字显示太过密集)
map1 = (Map(init_opts=opts.InitOpts(width='1900px', height='900px', bg_color='#ADD8E6', theme='white'))
        .add('死亡人数', [list(z) for z in zip(data['name'], data['total_dead'])], 'world', is_map_symbol_show=False)
        .set_global_opts(title_opts=opts.TitleOpts(title='2022年06月13日世界新冠死亡人数可视化'),
                         visualmap_opts=opts.VisualMapOpts(is_show=True,
                                                           min_=np.min(data['today_dead'].tolist()),
                                                           max_=np.min(data['today_dead'].tolist()),
                                                           range_text=['High', 'Low'], is_piecewise=True,
                                                           pieces=[{'min': 0, 'max': 100, 'label': '<100'},
                                                                   {'min': 100, 'max': 500, 'label': '100 - 500'},
                                                                   {'min': 500, 'max': 1000, 'label': '500 - 1000'},
                                                                   {'min': 1000, 'max': 10000, 'label': '1000 - 10000'},
                                                                   {'min': 10000, 'max': 20000, 'label': '10000 - 20000'},
                                                                   {'min': 20000, 'label': '> 500'},
                                                                   ])))
map1.render(path="./new_data/16、世界地图新冠死亡人数.HTML")  # 生成html
"""
