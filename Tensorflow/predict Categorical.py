# 범주형 데이터 다루기
# 범주형데이터-> 수치로 변환 (원핫인코딩)

import tensorflow as tf
import pandas as pd

# 데이터 준비
URL = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris = pd.read_csv(URL)
iris.head()

iris = pd.get_dummies(iris)  # 원핫인코딩
iris.head()

# 변수 나누기
print(iris.columns)
ehrflq = iris[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
whdthr = iris[['품종_setosa', '품종_versicolor',
               '품종_virginica']]

# 모델 구조만들기
x = tf.keras.layers.Input(shape=[4])
y = tf.keras.layers.Dense(3, activation='softmax')(x)
model = tf.keras.models.Model(x, y)
model.compile(loss='categorical_crossentropy',
              metrics='accuracy')

# 학습
model.fit(ehrflq, whdthr, epochs=10000, verbose=0)
model.fit(ehrflq, whdthr, epochs=10)

# 모델 이용
print(model.predict(ehrflq[0:5]))
print(whdthr[0:5])

# 학습한 가중치 보기
model.get_weights()
