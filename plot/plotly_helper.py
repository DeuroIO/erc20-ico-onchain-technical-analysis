import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('gelei', 'SYLSznL3X1AeEV724w1q')

def plot_helper(fig):
    try:
        plot_url = py.plot(fig)
        return plot_url
    except:
        print("failed to plot.retry...")
        return plot_helper(fig)

def plot_using_plotly(title,traces):
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
    plot_url = plot_helper(fig)

    print(title + " --- " + plot_url)
    return plot_url

def plot_top_50_list_using_plotly(title,traces):
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
        "title": "Amount"
      }
    }
    fig = Figure(data=data, layout=layout)
    plot_url = plot_helper(fig)
    
    print(title + " --- " + plot_url)
    return plot_url
# plot_using_plotly("RDN Top Investor",[trace1,trace2,trace3])
