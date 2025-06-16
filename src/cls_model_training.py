from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_classification_model(X_train, y_train):
    clf = GradientBoostingClassifier()
    clf.fit(X_train, y_train)
    return clf

def evaluate_classifier(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        'Accuracy': accuracy_score(y_test, preds),
        'Precision': precision_score(y_test, preds),
        'Recall': recall_score(y_test, preds),
        'F1-score': f1_score(y_test, preds)
    }
