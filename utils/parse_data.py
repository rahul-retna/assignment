from config import STAT_PATH
import pandas as pd

stat = pd.read_csv(STAT_PATH, index_col=0)

keys = [
    "age",
    "bmi",
    "children"
]

def parse_float(value):
    try:
        value = float(value)
    except:
        pass
    return value

def parse(request, item):
    value = parse_float(request.json[item])
    if item not in keys:
        return value
    else:
        avg = stat[item]['mean']
        std = stat[item]['std']
        return (value - avg) / std
