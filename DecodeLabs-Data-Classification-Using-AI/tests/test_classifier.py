import pathlib
import sys

PROJECT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from classifier import load_and_split_data, train_and_evaluate


def test_iris_split_is_80_20():
    iris, X_train, X_test, y_train, y_test = load_and_split_data()
    assert len(iris.data) == 150
    assert X_train.shape == (120, 4)
    assert X_test.shape == (30, 4)
    assert len(y_train) == 120
    assert len(y_test) == 30


def test_knn_pipeline_returns_required_metrics():
    result = train_and_evaluate(n_neighbors=5)
    assert 0.0 <= result.accuracy <= 1.0
    assert 0.0 <= result.precision <= 1.0
    assert 0.0 <= result.recall <= 1.0
    assert 0.0 <= result.f1_score <= 1.0
    assert len(result.confusion_matrix) == 3
    assert all(len(row) == 3 for row in result.confusion_matrix)


def test_model_performs_well_on_fixed_split():
    result = train_and_evaluate(n_neighbors=5)
    assert result.accuracy >= 0.90
