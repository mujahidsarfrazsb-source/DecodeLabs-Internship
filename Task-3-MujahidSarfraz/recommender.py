"""Content-based Tech Stack Recommender for DecodeLabs Project 3."""

import argparse
import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATASET_PATH = Path(__file__).resolve().parent / "data" / "raw_skills.csv"
MINIMUM_SKILLS = 3
DEFAULT_TOP_N = 3


def load_job_roles(csv_path: Path = DATASET_PATH) -> list[dict[str, str]]:
    """Load job roles and their skill descriptions from the project dataset."""
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        expected_columns = {"job_role", "skills"}
        if not expected_columns.issubset(reader.fieldnames or []):
            raise ValueError("Dataset must contain 'job_role' and 'skills' columns.")

        roles = [row for row in reader if row.get("job_role") and row.get("skills")]

    if not roles:
        raise ValueError("Dataset does not contain any job roles.")
    return roles


def parse_skills(raw_skills: str) -> list[str]:
    """Parse comma-separated input into at least three unique normalized skills."""
    skills = []
    seen = set()

    for value in raw_skills.split(","):
        skill = " ".join(value.strip().lower().split())
        if skill and skill not in seen:
            skills.append(skill)
            seen.add(skill)

    if len(skills) < MINIMUM_SKILLS:
        raise ValueError("Please provide at least three different skills separated by commas.")

    return skills


def recommend_roles(
    user_skills: list[str],
    roles: list[dict[str, str]] | None = None,
    top_n: int = DEFAULT_TOP_N,
) -> list[dict[str, object]]:
    """Rank job roles by TF-IDF cosine similarity to the user's skills."""
    if len(user_skills) < MINIMUM_SKILLS:
        raise ValueError("At least three skills are required for recommendation.")
    if top_n < 1:
        raise ValueError("top_n must be at least 1.")

    roles = roles or load_job_roles()
    role_documents = [role["skills"] for role in roles]
    user_document = ", ".join(user_skills)

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9+#.-]*\b",
    )
    vectors = vectorizer.fit_transform(role_documents + [user_document])

    role_vectors = vectors[:-1]
    user_vector = vectors[-1]
    scores = cosine_similarity(user_vector, role_vectors).flatten()

    ranked = sorted(
        (
            {
                "job_role": role["job_role"],
                "skills": role["skills"],
                "similarity": float(score),
            }
            for role, score in zip(roles, scores)
        ),
        key=lambda item: (-item["similarity"], item["job_role"]),
    )

    return ranked[: min(top_n, len(ranked))]


def print_recommendations(recommendations: list[dict[str, object]]) -> None:
    """Display ranked career paths in a readable format."""
    print("Top career path recommendations:")
    for index, item in enumerate(recommendations, start=1):
        score = float(item["similarity"])
        print(f"{index}. {item['job_role']} - match score: {score:.3f}")
        print(f"   Related skills: {item['skills']}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Recommend career paths from at least three user skills."
    )
    parser.add_argument(
        "--skills",
        help="Comma-separated skills, for example: Python, Cloud Computing, Automation",
    )
    args = parser.parse_args()

    raw_skills = args.skills
    if raw_skills is None:
        raw_skills = input("Enter at least three skills separated by commas: ")

    try:
        user_skills = parse_skills(raw_skills)
        recommendations = recommend_roles(user_skills, top_n=DEFAULT_TOP_N)
    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return

    print_recommendations(recommendations)


if __name__ == "__main__":
    main()
