import re
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report, accuracy_score

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


def evaluate_model(true_values, preds):
    print("Matrix de confusión: \n", confusion_matrix(true_values, preds))
    target_names = ["Normal flow",
                    "SYN Scan - aggressive",
                    "Denial of Service R-U-Dead-Yet",
                    "Denial of Service Slowloris"]
    print(classification_report(true_values, preds, target_names=target_names))
    print("recall_score: ", recall_score(true_values, preds, average=None))
    print("precision_score: ", precision_score(
        true_values, preds, average=None))
    print("f1_score: ", f1_score(true_values, preds, average=None))
    print("accuracy: ", accuracy_score(true_values, preds))
