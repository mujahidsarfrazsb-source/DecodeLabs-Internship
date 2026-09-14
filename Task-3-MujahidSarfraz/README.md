# DecodeLabs AI Recommendation Logic

## Project 3

This project implements a content-based Tech Stack Recommender. It maps a user's skills to job-role skill profiles and returns the three most relevant career paths.

The implementation uses TF-IDF to convert skill text into weighted vectors and cosine similarity to measure how closely each job role aligns with the user profile.

## Pipeline

1. Accept at least three user skills.
2. Load job roles and skill descriptions from `data/raw_skills.csv`.
3. Convert the role descriptions and user profile into the same TF-IDF vector space.
4. Calculate cosine similarity between the user vector and each job-role vector.
5. Sort the results from highest to lowest similarity.
6. Return the top three career paths.

## Files

```text
DecodeLabs-AI-Recommendation-Logic/
|-- README.md
|-- recommender.py
|-- requirements.txt
|-- data/
|   `-- raw_skills.csv
`-- tests/
    `-- test_recommender.py
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

Interactive input:

```bash
python recommender.py
```

Or provide the skills directly:

```bash
python recommender.py --skills "Python, Cloud Computing, Automation"
```

Example output format:

```text
Top career path recommendations:
1. <job role> - match score: <score>
   Related skills: <skills from the dataset>
2. <job role> - match score: <score>
   Related skills: <skills from the dataset>
3. <job role> - match score: <score>
   Related skills: <skills from the dataset>
```

## Dataset

`data/raw_skills.csv` contains job roles and their associated skills. It is kept inside the project so the recommender can run without downloading a separate dataset.

## Test

```bash
pytest -q
```

The tests verify dataset loading, the three-skill input requirement, result ranking, and Top-3 output behavior.
