"""Iris classification pipeline for DecodeLabs Project 2."""

from dataclasses import dataclass

from sklearn.datasets import load_iris
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


@dataclass
class ClassificationResult:
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    confusion_matrix: list[list[int]]
    report: str
    train_size: int
    test_size: int


def load_and_split_data(test_size: float = 0.20, random_state: int = 42):
    """Load Iris data, shuffle with a stratified 80/20 split, and scale features."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=test_size,
        random_state=random_state,
        shuffle=True,
        stratify=iris.target,
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return iris, X_train_scaled, X_test_scaled, y_train, y_test


def train_and_evaluate(n_neighbors: int = 5) -> ClassificationResult:
    """Train KNN on Iris data and return the required evaluation metrics."""
    iris, X_train, X_test, y_train, y_test = load_and_split_data()

    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision, recall, f1_score, _ = precision_recall_fscore_support(
        y_test,
        predictions,
        average="macro",
        zero_division=0,
    )
    matrix = confusion_matrix(y_test, predictions)
    report = classification_report(
        y_test,
        predictions,
        target_names=iris.target_names,
        zero_division=0,
    )

    return ClassificationResult(
        accuracy=accuracy,
        precision=precision,
        recall=recall,
        f1_score=f1_score,
        confusion_matrix=matrix.tolist(),
        report=report,
        train_size=len(y_train),
        test_size=len(y_test),
    )


def main() -> None:
    iris = load_iris()
    result = train_and_evaluate(n_neighbors=5)

    print("DecodeLabs Data Classification Using AI")
    print(f"Dataset: Iris ({len(iris.data)} samples, {iris.data.shape[1]} features, {len(iris.target_names)} classes)")
    print(f"Training samples: {result.train_size}")
    print(f"Testing samples: {result.test_size}")
    print("Algorithm: K-Nearest Neighbors (K=5)")
    print("Feature scaling: StandardScaler")
    print(f"Accuracy: {result.accuracy:.4f}")
    print(f"Macro Precision: {result.precision:.4f}")
    print(f"Macro Recall: {result.recall:.4f}")
    print(f"Macro F1 Score: {result.f1_score:.4f}")
    print("Confusion Matrix:")
    for row in result.confusion_matrix:
        print(row)
    print("Classification Report:")
    print(result.report)


if __name__ == "__main__":
    main()
