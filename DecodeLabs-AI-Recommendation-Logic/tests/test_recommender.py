import pathlib
import sys

PROJECT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from recommender import load_job_roles, parse_skills, recommend_roles


def test_dataset_loads_job_roles():
    roles = load_job_roles()
    assert len(roles) >= 3
    assert all("job_role" in role and "skills" in role for role in roles)


def test_parse_skills_requires_three_unique_values():
    assert parse_skills("Python, SQL, Machine Learning") == [
        "python",
        "sql",
        "machine learning",
    ]

    try:
        parse_skills("Python, Python, SQL")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected fewer than three unique skills to be rejected.")


def test_recommender_returns_three_ranked_results():
    recommendations = recommend_roles(
        ["python", "sql", "machine learning"],
        top_n=3,
    )
    assert len(recommendations) == 3
    scores = [item["similarity"] for item in recommendations]
    assert scores == sorted(scores, reverse=True)
    assert recommendations[0]["job_role"] in {"Data Scientist", "Machine Learning Engineer"}
    assert recommendations[0]["similarity"] > 0
