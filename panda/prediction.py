import tensorflow as tf
import pandas as pd

URL = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
lemon = pd.read_csv(URL)
lemon.head()

Dependentvariable = lemon[['판매량']]  # 종속변수
Independencevariable = lemon[['온도']]  # 독립변수

x = tf.keras.layers.Input(shape=1)
y = tf.keras.layers.Dense(1)(x)
model = tf.keras.models.Model(x, y)
model.compile(loss='mse')

model.fit(Independencevariable, Dependentvariable, epochs=1000, verbose=0)
model.predict(Independencevariable)
print(model.predict([14]))
