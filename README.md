# DecodeLabs Internship

This repository contains three Artificial Intelligence projects completed for the DecodeLabs Industrial Training program, Batch 2026. Each project is kept in its own folder with separate source code, requirements, tests, and documentation.

## Projects

### 1. DecodeLabs-Rule-Based-AI-Chatbot
A command-line chatbot built with Python control flow and a rule-based response dictionary. It normalizes user input, responds to known intents, provides a fallback for unknown input, runs continuously, and exits cleanly when an exit command is entered.

### 2. DecodeLabs-Data-Classification-Using-AI
A supervised learning project using the Iris dataset. The project loads and inspects the data, performs an 80/20 train-test split, standardizes the feature values, trains a K-Nearest Neighbors classifier with K=5, and evaluates the model with accuracy, a confusion matrix, precision, recall, and F1 score.

### 3. DecodeLabs-AI-Recommendation-Logic
A content-based Tech Stack Recommender. The program accepts at least three user skills, converts job-role skills and the user profile into TF-IDF vectors, calculates cosine similarity, ranks the available career paths, and returns the top three matches.

## Repository Structure

```text
DecodeLabs-Internship/
|-- README.md
|-- .gitignore
|-- DecodeLabs-Rule-Based-AI-Chatbot/
|   |-- README.md
|   |-- chatbot.py
|   `-- tests/
|       `-- test_chatbot.py
|-- DecodeLabs-Data-Classification-Using-AI/
|   |-- README.md
|   |-- classifier.py
|   |-- requirements.txt
|   `-- tests/
|       `-- test_classifier.py
`-- DecodeLabs-AI-Recommendation-Logic/
    |-- README.md
    |-- recommender.py
    |-- requirements.txt
    |-- data/
    |   `-- raw_skills.csv
    `-- tests/
        `-- test_recommender.py
```

## Running the Projects

Open the folder for the project you want to run and follow its README. Projects 2 and 3 require packages listed in their local `requirements.txt` files. Project 1 uses the Python standard library only.

## Python Version

Python 3.10 or newer is recommended.
