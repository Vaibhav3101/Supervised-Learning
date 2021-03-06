from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
# print('--------------')
from sklearn.model_selection import train_test_split
# print('--------------')

iris = datasets.load_iris()
X=iris['data']
y=iris['target']
# X=iris.data
# y=iris.target
knn=KNeighborsClassifier(n_neighbors=8)
# print('--------------')
# knn.fit(iris['data'],iris['target'])
# print('--------------')

X_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=2,stratify=y)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

print(y_pred)
## Calculating Accuracy Score
knn.score(X_test,y_test)