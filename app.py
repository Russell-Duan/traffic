from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objs as go
import networkx as nx

import sqlite3

app = Flask(__name__)

def time_estimation(G, df, start_node, end_node, w_of_day, h_of_day, wk_coef):
    time_estimation = 0

    path_list = []
    path = nx.shortest_path(
        G=G,
        source=start_node,
        target=end_node)
    temp = path[0][0:4]
    path_list.append(temp)
    for key in path:
        if key[0:4] != temp:
            temp = key[0:4]
            path_list.append(temp)

    for i in range(len(path_list) - 1):
        if len(df.loc[(df['sourceid'] == int(path_list[i])) & (df['dstid'] == int(path_list[i + 1])) & (df['hod'] == h_of_day)]['mean_travel_time']) == 0:
            if len(df.loc[(df['sourceid'] == int(path_list[i])) & (df['dstid'] == int(path_list[i + 1]))]) == 0:
                time_estimation += float(df.loc[(df['sourceid'] == int(path_list[i]))]['mean_travel_time'].min())
            else:
                time_estimation += float(df.loc[(df['sourceid'] == int(path_list[i])) & (df['dstid'] == int(path_list[i + 1]))]['mean_travel_time'].mean())
        else:
            time_estimation += float(df.loc[(df['sourceid'] == int(path_list[i])) & (df['dstid'] == int(path_list[i + 1])) & (df['hod'] == h_of_day)]['mean_travel_time'])

    time_estimation = wk_coef[w_of_day] * time_estimation

    return str(round(time_estimation / 60, 2)) + " minutes"


def shortest_path_plot(G, start_node, end_node):
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line={'width': 0.5, 'color': '#888'},
        hoverinfo='text',
        mode='lines')

    fig = go.Figure(data=edge_trace,
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    path = nx.shortest_path(
        G=G,
        source=start_node,
        target=end_node)

    path_x = []
    path_y = []
    for key in path:
        x0, y0 = G.nodes[key]['pos']
        path_x.append(x0)
        path_y.append(y0)

    fig.add_trace(go.Scatter(x=path_x,
                             y=path_y,
                             line=dict(width=5, color='blue'),
                             hoverinfo='none',
                             mode='lines'))

    return fig

@app.route('/')
def main_page():
    fig = plotly.io.read_json('C:/Users/duanh/OneDrive/Documents/GitHub/traffic-density/data/graph.json')
    fig.update_layout(
        showlegend=False,
        autosize=False,
        width=800,
        height=800,
        margin=dict(
            l=50,
            r=50,
            b=10,
            t=100,
            pad=4))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('main.html', graphJSON=graphJSON)

@app.route('/', methods=['POST'])
def parse_urls():
    if request.method == 'POST':
        start_node = str(request.form['from'])+'-0-0'
        end_node = str(request.form['to'])+'-0-0'
        w_of_day = int(request.form['dow'])
        h_of_day = int(request.form['hod'])
        df = pd.read_csv("C:/Users/duanh/OneDrive/Documents/GitHub/traffic-density/data/los_angeles-censustracts-2018-2-All-HourlyAggregate.csv")
        wk = pd.read_csv("C:/Users/duanh/OneDrive/Documents/GitHub/traffic-density/data/los_angeles-censustracts-2018-1-WeeklyAggregate.csv")
        wk_coef = wk.groupby(['dow'])['mean_travel_time'].mean() / wk.groupby(['dow'])['mean_travel_time'].mean()[7]
        G = nx.read_gpickle("C:/Users/duanh/OneDrive/Documents/GitHub/traffic-density/data/graph.gpickle")
        fig = shortest_path_plot(G=G, start_node=start_node, end_node=end_node)
        time = time_estimation(G=G, df=df, start_node=start_node, end_node=end_node, w_of_day=w_of_day, h_of_day=h_of_day, wk_coef=wk_coef)
        fig.update_layout(
            showlegend=False,
            autosize=False,
            width=800,
            height=800,
            margin=dict(
                l=50,
                r=50,
                b=10,
                t=100,
                pad=4))
        graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('submit.html', time=time, graph=graph)