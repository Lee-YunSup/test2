import numpy as np
import h_prepro

def h_split(data_x, data_y):
    train_size = int(len(data_y) * 0.8)
    train_x = np.array(data_x[0 : train_size])
    train_y = np.array(data_y[0 : train_size])

    test_size = len(data_y) - train_size
    test_x = np.array(data_x[train_size : len(data_x)])
    test_y = np.array(data_y[train_size : len(data_y)])
    return train_x, train_y, test_x, test_y