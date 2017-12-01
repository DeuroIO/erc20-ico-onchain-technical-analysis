import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('gelei', 'SYLSznL3X1AeEV724w1q')

def plot_helper(fig,filename,trails=0,max_trail=5):
    if trails >= max_trail: return ""
    try:
        plot_url = py.plot(fig,filename=filename)
        return plot_url
    except Exception as e:
        print(e)
        print("failed to plot.retry...")
        return plot_helper(fig,filename,trails=trails+1)

def plot_using_plotly(title,traces,filename):
    data = Data(traces)
    layout = {
      "autosize": True,
      "height": 1000,
      "showlegend": True,
      "title": title,
      "width": 2000,
      "xaxis": {
        "autorange": True,
        "title": "Time (days)",
      },
      "yaxis": {
        "autorange": True,
        "title": "Token Amount"
      },
      "yaxis2":{
        "title":'Price(USD)',
        "overlaying":'y',
        "side":'right'
        }
    }
    fig = Figure(data=data, layout=layout)
    plot_url = plot_helper(fig,filename)

    print(title + " --- " + plot_url)
    return plot_url
# plot_using_plotly("RDN Top Investor",[trace1,trace2,trace3])
