import h_tolist

def h_prepro(x,y):
    window_size = 5
    data_x, data_y = [], []

    for i in range(len(y) - window_size):
        _x = x[i:i+window_size]
        _y = y[i+window_size]
        data_x.append(_x)
        data_y.append(_y)
    return data_x, data_y