import pandas as pd
import numpy as np


chat_id = 539377624 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = np.array([0] * 40)
    for i in range(40):
        a[i] = 2.0 * x[i] / n[i] / n[i]
    return a.mean()
