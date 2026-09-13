# DecodeLabs Data Classification Using AI

## Project 2

This project builds a basic supervised classification pipeline using the Iris dataset and a K-Nearest Neighbors classifier.

The Iris dataset contains 150 balanced samples, three classes, and four numeric features. The implementation follows an input-process-output workflow: load and prepare the data, train the classifier, then evaluate the predictions.

## Pipeline

1. Load the Iris dataset.
2. Split the dataset into 80% training data and 20% testing data.
3. Shuffle the samples and preserve class balance with a stratified split.
4. Fit `StandardScaler` on the training features and transform both sets.
5. Train `KNeighborsClassifier` with `K=5`.
6. Predict the test set classes.
7. Report accuracy, confusion matrix, precision, recall, and F1 score.

## Files

```text
DecodeLabs-Data-Classification-Using-AI/
|-- README.md
|-- classifier.py
|-- requirements.txt
`-- tests/
    `-- test_classifier.py
```

## Setup

From this project folder:

```bash
python -m venv .venv
```

Activate the virtual environment, then install the required packages:

```bash
pip install -r requirements.txt
```

## Run

```bash
python classifier.py
```

The program prints the dataset size, train-test sizes, algorithm settings, evaluation metrics, confusion matrix, and classification report.

## Test

```bash
pytest -q
```

The tests verify the 80/20 split, the expected Iris dimensions, the evaluation output, and the model performance on the fixed split.
