
import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np


app = dash.Dash()

cmds = ['me', 'mu', 'mo', 'ma']


times = [i for i in range(0,101)]
data = [np.random.randint(1,101) for i in range(0,101)]

if __name__ == '__main__':
    app.run_server(debug=False)