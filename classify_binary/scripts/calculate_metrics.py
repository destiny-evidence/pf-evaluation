from typing import List
import json

from promptflow.core import log_metric, tool
from sklearn.metrics import f1_score, precision_score, recall_score


@tool
def calculate_accuracy(y_true: List[bool], pred: List[str]):      

    y_pred = [json.loads(x)['relevance'] for x in pred]


    metrics = {
        'f1_score': f1_score(y_true, y_pred),
        'precision_score': precision_score(y_true, y_pred),
        'recall_score': recall_score(y_true, y_pred)
    }
    for key, value in metrics.items():
        log_metric(key, value)

    return metrics