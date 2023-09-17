import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from pydantic import BaseModel
import cv2


""" Класс Iris наследуется от BaseModel для аннотации атрибутов класса"""

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    
class Detector(BaseModel):
    img_path: str
    
class IrisClassifier:
    def __init__(self) -> None:
        self.X, self.y = load_iris(return_X_y=True)
        self.clf = self.train_model()
        self.iris_type = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

    def train_model(self) -> LogisticRegression:
        return LogisticRegression(solver='lbfgs',
                                  max_iter=1000,
                                  multi_class='multinomial').fit(self.X, self.y)

    def classify_iris(self, iris: Iris):
        X = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]
        prediction = self.clf.predict_proba([X])
        return {'class': self.iris_type[np.argmax(prediction)],
                'probability': round(max(prediction[0]), 2)}
        
class FaceDetector:
    
    """ Написать модель машинного обучения для детекции лица человека. Модель основана на каскаде Хаара """
    def __init__(self, img_path: Detector) -> None:
        self.image = cv2.imread(img_path)
    pass