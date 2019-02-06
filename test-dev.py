import sys
import time
import matplotlib.pyplot as plt
import numpy as np


class Sample:
    def __init__(self):
        self.x = 2
        self.y = 3
sample_object = Sample()

from modelchimp import Tracker
tracker = Tracker('<key>', host='127.0.0.1:8000', experiment_name='sample_name 6')

time.sleep(2)
tracker.add_param("test_param", "jd934")
tracker.add_custom_object("custom", sample_object)
tracker.add_multiple_params({'x': 1, 'y': 'Hello'})
tracker.add_multiple_metrics({'x': 1, 'y': 2}, 1)
tracker.add_multiple_metrics({'x': 3, 'y': 1}, 2)
tracker.add_dataset_id("XYZ")
tracker.add_metric("accuracy", 0.8,1)
tracker.add_metric("precision", 0.83,1)
tracker.add_metric("recall", 0.91, 1)
tracker.add_duration_at_epoch("train", 3000, 1)
tracker.add_duration_at_epoch("test", 3540, 1)
tracker.add_image('./dog.0.jpg', {'accuracy': 0.98, 'precision': 0.70}, epoch=2)

def get_matplot():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2*np.pi*t)
    plt.plot(t, s)

    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")

    return plt

tracker.add_custom_plot("Test Plot", get_matplot())
