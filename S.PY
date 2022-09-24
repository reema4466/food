import selectors
from keras.models import Sequential
from keras. layers import Dense
from keras. layers import LSTM
from sklearn.model_selection import train_test_split
model = Sequential()
model.add (LSTM(10, input_shape=(1, 1)))
model.add (Dense(l, activation="linear") )
model.compile(loss="mse", optimizer="adam")
X, y = get_data( )
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train_2, X_val, y_train_2, y_val=train_test_split(X_train, y_train, test_size=0.25, random_state=1
)
model.fit(X_train, y_train, epochs=800, validation_data=(X_val, y_val), shuffle=False)