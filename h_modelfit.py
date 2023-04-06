import h_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

def h_modelfit(train_x,train_y,test_x):
    model = Sequential()
    model.add(LSTM(20,activation='relu',return_sequences=True, input_shape=(5,1)))
    model.add(LSTM(units=40, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(train_x, train_y, epochs=10)

    pred_y = model.predict(test_x)

    return pred_y