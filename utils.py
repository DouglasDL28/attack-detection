import re

import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
from yellowbrick.classifier import ROCAUC

from sklearn.metrics import (confusion_matrix, auc, precision_score, recall_score,
                             f1_score, classification_report, accuracy_score, roc_curve, auc)

nums_regex = re.compile(r"[0-9]+")


def normalize_dst_to_src_column(value):
    result = list(filter(lambda v: v != "", nums_regex.findall(str(value))))
    if len(result) == 0:
        return 0
    result = [int(x) for x in result]
    return sum(result)


def lematize_protocol(protocol):
    if "." in protocol:
        index = protocol.index(".")
        return protocol[:index]
    return protocol


def is_int(val):
    try:
        int(val)
        return True
    except:
        return False


def evaluate_model(y_true, y_pred):
    target_names = ["Normal flow",
                    "SYN Scan - aggressive",
                    "Denial of Service R-U-Dead-Yet",
                    "Denial of Service Slowloris"]
    print("Matrix de confusión: \n", confusion_matrix(y_true, y_pred))
    print(classification_report(y_true, y_pred, target_names=target_names))
    print("recall_score: ", recall_score(y_true, y_pred, average=None))
    print("precision_score: ", precision_score(
        y_true, y_pred, average=None))
    print("f1_score: ", f1_score(y_true, y_pred, average=None))
    print("accuracy: ", accuracy_score(y_true, y_pred))


def plot_roc_curve(model, X_train, y_train, X_test, y_test):

    # Creating visualization with the readable labels
    visualizer = ROCAUC(model, encoder={0: 'Normal flow', 
                                        1: 'SYN Scan - aggressive', 
                                        2: 'Denial of Service R-U-Dead-Yet',
                                        3: 'Denial of Service Slowloris'})
                                        
    # Fitting to the training data first then scoring with the test data                                    
    visualizer.fit(X_train, y_train)
    visualizer.score(X_test, y_test)
    visualizer.show()
    
    return visualizer

