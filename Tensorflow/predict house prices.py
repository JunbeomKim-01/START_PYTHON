import tensorflow as tf
import pandas as pd


URL = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston = pd.read_csv(URL)

print(boston.columns)
boston.head()

# 변수 분리
ehrflq = boston[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
                 'ptratio', 'b', 'lstat']]

whdthr = boston[['medv']]
print(ehrflq.shape, whdthr.shape)

# 모델 구조 만들기
x = tf.keras.layers.Input(shape=[13])
y = tf.keras.layers.Dense(1)(x)
model = tf.keras.models.Model(x, y)
model.compile(loss='mse')

# 학습
model.fit(ehrflq, whdthr, epochs=1000000, verbose=0)
model.fit(ehrflq, whdthr, epochs=10)

# 확인
model.predict(ehrflq[0:5])
print(model.predict(ehrflq[5:10]))

# 수식 확인
model.get_weights()
