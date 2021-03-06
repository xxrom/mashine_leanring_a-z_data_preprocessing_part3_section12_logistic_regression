# Logistic Regression
# по факту, алгоритм просто рисует линейную регрессию для 0, 1 элементов
# все что выходит за границы между 0 и 1 будет равно 0 или 1 соответсвенно
# и потом по этой ломанной прямой вписывают atan(опционально, тут нет этого)
# и по этой кривой можно определить вероятность того, что человек с такими
# параметрами купит или не купит какую-либо штуковину

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
# TODO: Почему нужно здесь делать масштабирование ?????????
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0) # инициализация модели
classifier.fit(X_train, y_train) # закидываем в модель данные для обучения модели

# Predicting the Test set results
y_pred = classifier.predict(X_test) # предсказываем данные из X_test

# Making the Confusion Matrix # узнаем насколько правильная модель
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred) # закиыдваем тестовые и предсказанные данные
# данные [[65, 3], [8, 24]] 65+24= правильных предсказаний, 3+8= неправильных, в сумме будет 100 (y_test)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train

# подготавливаем матрицу для нашего поля данных с шагом сетки 0.01
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))

# вся магия тут, раскрашиваем данные по всему полотку X1, X2
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green')))

# границы для областей указываем?
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

# все точки рисуем на полотне, которые у нас есть
for i, j in enumerate(np.unique(y_set)):
  plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
              c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend() # в правом верхнем углу рисует соотношение точек и из значений
plt.show()






























































