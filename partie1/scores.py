
import json
from pathlib import Path


SCORES_FILE = Path(__file__).parent / "scores.json"


def load_scores():
    if not SCORES_FILE.exists():
        return []

    try:
        with open(SCORES_FILE, "r", encoding="utf-8") as file:
            scores = json.load(file)

        if isinstance(scores, list):
            return scores

        return []

    except (OSError, json.JSONDecodeError):
        return []


def save_score(score):
    scores = load_scores()
    scores.append(score)

    with open(SCORES_FILE, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4)


def get_record():
    scores = load_scores()
    return max(scores, default=0)
