from pathlib import Path

from planify.ingest import extract_text
from planify.planner import PlanifyEngine

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "samples" / "ml_notes.txt"


def test_light_plan_has_days():
    text = extract_text(SAMPLE)
    plan = PlanifyEngine(use_models=False).build_plan(text, num_days=3, minutes_per_day=45)
    assert len(plan.days) == 3
    assert plan.summary
    assert plan.questions
    md = plan.to_markdown()
    assert "Day 1" in md
