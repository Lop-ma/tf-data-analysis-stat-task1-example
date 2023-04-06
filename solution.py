import pandas as pd
import numpy as np


chat_id = 539377624 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    for i in range(len(x)):
        x[i] = 2.0 * x[i] / 40 / 40
    return x.mean()
