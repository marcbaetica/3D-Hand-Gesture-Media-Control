import subprocess
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from functools import partial
from threading import Thread
from time import sleep


AVAILABLE_PLOT_TYPES = ['time_series']  # Do not change elements order.


class AudioPlot:
    def __init__(self, type, frames_count):
        self.type = type
        if self.type == AVAILABLE_PLOT_TYPES[0]:
            self.doc, self.source = self.generate_time_series_plot(frames_count)
        else:
            raise ValueError(f'Only plots of type {AVAILABLE_PLOT_TYPES} are acceptable. Received: {self.type}.')
        self.display_plot()

    @staticmethod
    def generate_time_series_plot(frames_count):
        data_points = [0 for _ in range(frames_count)]
        source = ColumnDataSource(data={
            'x': [i for i in range(len(data_points))],
            'y': data_points[0]
        })
        plot = figure(width=1500, height=700)
        plot.line(x='x', y='y', source=source)
        doc = curdoc()
        doc.add_root(plot)
        return doc, source

    @staticmethod
    def display_plot():
        subprocess.run(['bokeh', 'serve', '--show', 'time_series_audio_plot.py'])
        # TODO: Maybe set it up as a flask app like: https://github.com/bokeh/bokeh/blob/2.4.2/examples/howto/ajax_source.py

    def _update_source_with_new_frame_data(self, new_data):
        self.source.data['y'] = new_data

    def update_source_blocking_task(self, new_data):
        self.doc.add_next_tick_callback(partial(self._update_source_with_new_frame_data, new_data))


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
