from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

#load the diabetes dataset
iris_X, iris_y = datasets.load_iris(return_X_y=True)

#define model
dt_classifier = DecisionTreeClassifier()

#train
dt_classifier.fit(iris_X, iris_y)

#split train : test = 8 : 2
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.2, random_state = 42)