import subprocess
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from functools import partial
from threading import Thread
from time import sleep


# class TimeSeriesAudioPlot:
#     @classmethod
#     def create_time_series_plot(cls):
#         print()


def read_data_points_set_from_file(file):
    with open(file, 'r') as f:
        return [eval(line.rstrip()) for line in f.readlines()]


def update_new_frame_data(new_data):
    source.data['y'] = new_data


def blocking_task():
    for data_points in data_points_set:
        sleep(1)
        doc.add_next_tick_callback(partial(update_new_frame_data, data_points))


data_points_set = read_data_points_set_from_file('sample_data.txt')
source = ColumnDataSource(data={
    'x': [i for i in range(len(data_points_set[0]))],
    'y': data_points_set[0]
})
plot = figure(width=1500, height=700)
plot.line(x='x', y='y', source=source)


doc = curdoc()
doc.add_root(plot)
thread = Thread(target=blocking_task)
thread.start()


subprocess.run(['bokeh', 'serve', '--show', 'time_series_audio_plot.py'])
# TODO: Maybe set it up as a flask app like: https://github.com/bokeh/bokeh/blob/2.4.2/examples/howto/ajax_source.py
