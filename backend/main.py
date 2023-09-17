from fastapi import FastAPI
from backend.model import (IrisClassifier, Iris, Detector)
from starlette.responses import JSONResponse

app = FastAPI(description=""" 
                This API was made for MAI university project
              """)

@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Iris classifier is all ready to go!'

@app.post('/classify_iris')
def predict_iris(iris_features: Iris):
    iris_classifier = IrisClassifier()
    return JSONResponse(iris_classifier.classify_iris(iris_features))

@app.post('/detect_face')
def detect(detector_features: Detector):
    pass
    


    
    