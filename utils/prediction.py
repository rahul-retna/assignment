import numpy as np
from pickle import load as pickle_load
from config import MODEL_PATH

model = None
try:
    model = pickle_load(open(MODEL_PATH, "rb"))
except:
    model = None

def predict_charge(age, sex, bmi, children, smoker, region):
    charge = None
    try:
        charge = model.predict(np.array([[age, sex, bmi, children, smoker, region]]))[0]
    except:
        charge = None
    return charge
