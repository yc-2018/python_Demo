import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5, 6, 7],
    y=[8, 10, 12, 14, 16, 18, 20],
    mode='markers',
    marker=dict(size=[10, 14, 16, 18, 20, 42, 64],)  # 设置气泡大小
    )

data = [trace0]

go.Funnel(data)
pyplt(data, filename='1.html')
