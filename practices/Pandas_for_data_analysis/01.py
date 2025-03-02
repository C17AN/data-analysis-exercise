from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris
