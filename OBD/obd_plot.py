# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# df = pd.DataFrame.from_csv('obd_test.txt', index_col=None)

# kph = df['KPH']
# rpm = df['RPM']
# throttle = df['Throttle']

# kph.plot()
# plt.show()

# rpm.plot()
# plt.show()

# throttle.plot()
# plt.show()

import dash
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader.data import DataReader
import time
from collections import deque, defaultdict
import plotly.graph_objs as go
import obd
import numpy as np

use_obd = False;

if use_obd:
    connection = obd.OBD()

app = dash.Dash('OBD')

# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True

max_length = 50
# ENGINE_LOAD   19.215686274509803
# COOLANT_TEMP   88
# RPM   750.0
# SPEED   0
# THROTTLE_POS   3.9215686274509802
# FUEL_LEVEL
if use_obd:
    bad_keys = ['modes', 'OBD_COMPLIANCE', 'ELM_VERSION', 'ELM_VOLTAGE']
    cmds = {key: cmd for key, cmd in obd.commands.__dict__.items() if key not in bad_keys and connection.supports(cmd)}
else:
    cmds = ['me', 'mu', 'mo', 'ma']

times = deque(maxlen=max_length)
plot_data = defaultdict(lambda: deque(maxlen=max_length))

def update_obd_values(data_names):
    global plot_data
    global times
    times.append(time.time())
    if use_obd:
        if connection.is_connected():
            for cmd in data_names:
                val = connection.query(obd.commands[cmd]).value
                val = float(val.split()[0])
                plot_data[cmd].append(val)
    else:
        for cmd in data_names:
            val = np.random.randint(1,101)
            plot_data[cmd].append(val)

app.layout = html.Div([
    # html.Link(
    #     rel='stylesheet',
    #     href='/static/style.css'),
    html.Link(
        rel='stylesheet',
        href='/static/materialize.css'),
    html.Div([
        html.H2('Vehicle Data', style={'float':'left',}),
        ]),
    dcc.Dropdown(id='vehicle-data-name',
                 options=[{'label': s, 'value': s}
                            for s in cmds],
                 value=[cmds[0]],
                 multi=True),
    html.Div(children=html.Div(id='graphs'), className='row'),
    # html.Div(id='graphs', className='row'),

    dcc.Interval(
        id='graph-update',
        interval=100)
    ], className='container',
    style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})


@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('vehicle-data-name','value')],
    events=[dash.dependencies.Event('graph-update','interval')]
    )
def update_graph(data_names):
    graphs = []

    update_obd_values(data_names)

    if len(data_names) > 2:
        class_choice = 'col s12 m6 l4'
    else:
        class_choice = 'col s12 m6 l6'

    for data_name in data_names:
        data = go.Scatter(
            x=list(times),
            y=list(plot_data[data_name]),
            name='Scatter',
            fill='tozeroy',
            fillcolor='#6897bb')

        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            figure={'data':[data],
                    'layout':go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                       yaxis=dict(range=[min(plot_data[data_name]), max(plot_data[data_name])]),
                                       margin={'l':50,'r':1,'t':45,'b':1},
                                       title='{}'.format(data_name))}
            ), className=class_choice))
    return graphs


# external_css = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.css']
external_css = ['/static/materialize.css']

for css in external_css:
    app.css.append_css({'external_url': css})

# external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
# for js in external_js:
#     app.scripts.append_script({'external_url': js})

if __name__ == '__main__':
    app.run_server(debug=True)
