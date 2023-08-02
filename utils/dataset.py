import numpy as np
import tensorflow as tf


# dataset class
class Dataset:
    def __init__(self, x_shape: tuple = None, y_shape: tuple = None):
        self.x_shape = x_shape
        self.y_shape = y_shape
        self.data = []
        self.count = 0

    # add case with label
    def add_sample(self, x, y):
        if self.x_shape is None and self.y_shape is None:
            self.x_shape = x.shape
            self.y_shape = y.shape

        if x.shape != self.x_shape or y.shape != self.y_shape:
            raise AttributeError(f"Wrong input or output shape: X must be {self.x_shape} - given {x.shape}; "
                                 f"Y must be {self.y_shape}; given {y.shape}")

        self.data.append((x, y))
        self.count += 1

    # save dataset to file
    def save_to_file(self, path):
        if len(self.data) == 0:
            return

        data, labels = zip(*self.data)
        data = np.array(data)
        labels = np.array(labels)

        dataset = tf.data.Dataset.from_tensor_slices((data, labels))
        tf.data.Dataset.save(dataset, path)

    # get amount of samples in dataset
    def get_count(self):
        return self.count

    # load dataset from file
    @staticmethod
    def load_from_file(path):
        try:
            loaded_dataset = tf.data.Dataset.load(path)
            x, y = list(loaded_dataset.take(1).as_numpy_iterator())[0]
            d = Dataset(x.shape, y.shape)
            d.data = list(loaded_dataset.as_numpy_iterator())
            d.count = len(d.data)
            return d
        except UnicodeDecodeError:
            print("Wrong dir")
            return Dataset()

