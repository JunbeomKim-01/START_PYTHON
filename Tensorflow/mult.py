import tensorflow as tf
import pandas as pd

URL = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston = pd.read_csv(URL)
boston.head()
print(boston.shape)

ehrflq = boston[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
                 'ptratio', 'b', 'lstat']]
whdthr = boston[['medv']]

print(ehrflq.columns, whdthr.columns)

x = tf.keras.layers.Input(shape=[13])
h = tf.keras.layers.Dense(8, activation='swish')(x)
h = tf.keras.layers.Dense(8, activation='swish')(h)
h = tf.keras.layers.Dense(8, activation='swish')(h)
y = tf.keras.layers.Dense(1)(h)
model = tf.keras.models.Model(x, y)
model.compile(loss='mse')

model.fit(ehrflq, whdthr, epochs=10000, verbose=0)
model.fit(ehrflq, whdthr, epochs=10)
