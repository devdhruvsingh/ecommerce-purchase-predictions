from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
)


def evaluate_model(model, X_test, y_test):
    """Evaluate a trained classification model."""

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print("Accuracy :", accuracy_score(y_test, predictions))
    print("Precision:", precision_score(y_test, predictions))
    print("Recall   :", recall_score(y_test, predictions))
    print("F1 Score :", f1_score(y_test, predictions))
    print("ROC-AUC  :", roc_auc_score(y_test, probabilities))

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    return {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
        "f1": f1_score(y_test, predictions),
        "roc_auc": roc_auc_score(y_test, probabilities),
    }
