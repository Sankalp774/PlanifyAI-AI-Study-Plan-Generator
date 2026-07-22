"""CLI: python -m planify.cli notes.txt --days 5"""

from __future__ import annotations

import argparse
import json
import os

from planify.ingest import extract_text
from planify.planner import PlanifyEngine


def main() -> None:
    p = argparse.ArgumentParser(description="PlanifyAI CLI")
    p.add_argument("path", help="Document path")
    p.add_argument("--days", type=int, default=5)
    p.add_argument("--minutes", type=int, default=60)
    p.add_argument("--light", action="store_true", help="No transformer downloads")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    light = args.light or os.environ.get("PLANIFY_LIGHT") == "1"
    text = extract_text(args.path)
    plan = PlanifyEngine(use_models=not light).build_plan(
        text, num_days=args.days, minutes_per_day=args.minutes
    )
    if args.json:
        print(json.dumps(plan.to_dict(), indent=2))
    else:
        print(plan.to_markdown())


if __name__ == "__main__":
    main()
