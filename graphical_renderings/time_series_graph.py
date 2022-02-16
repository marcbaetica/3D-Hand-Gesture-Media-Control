import ast
import json
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.resources import INLINE
from flask import Flask, request, Response
from jinja2 import Template


app = Flask(__name__)

source = ColumnDataSource({
            'x': [i for i in range(1024)],
            'y': [0 for _ in range(1024)]   # TODO: Parameterize batch size.
         })

template = Template('''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Streaming Example</title>
        {{ js_resources }}
        {{ css_resources }}
    </head>
    <body>
    {{ plot_div }}
    {{ plot_script }}
    </body>
</html>
''')


@app.route('/')
def graph_page():
    global source
    plot = figure()
    plot.line(x='x', y='y', source=source)
    script, div = components(plot, INLINE)
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    html = template.render(
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources
    )
    return html


@app.route('/set-new-data', methods=['POST'])
def set_new_data():
    global source
    # source.data['y'] = ast.literal_eval(json.loads(request.data)['new_batch'])
    # source.stream({'y': [randint(0, 1000) for _ in range(10)], 'x': [i for i in range(10)]}, rollover=1024)
    # source.patch({'y': [(slice(1024), ast.literal_eval(json.loads(request.data)['new_batch']))]})
    source.data = {'x': source.data['x'], 'y': ast.literal_eval(json.loads(request.data)['new_batch'])}
    return Response(status=200)


def run_flask_server():
    app.run(port=5001)
