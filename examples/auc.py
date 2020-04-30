import pandas as pd
from sklearn import metrics


def auc():
    data = pd.read_csv("darpa_labels.txt", names=["label"])
    # data = data.head()

    methods = ["midas"]
    for i in range(len(methods)):
        scores = pd.read_csv("scores.txt", header=None, squeeze=True)
        fpr, tpr, _ = metrics.roc_curve(data.label, scores)
        auc = metrics.roc_auc_score(data.label, scores)
        print("AUC: ", auc)


if __name__ == "__main__":
    auc()
