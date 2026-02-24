#!/usr/bin/env python3
"""Validate publication mappings in _data/publications.yml."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


def main() -> int:
    publications_file = Path(__file__).resolve().parents[1] / "_data" / "publications.yml"
    data = yaml.safe_load(publications_file.read_text(encoding="utf-8")) or {}

    items = data.get("items")
    by_project = data.get("by_project")

    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(items, dict):
        errors.append("`items` must be a mapping.")
        items = {}
    if not isinstance(by_project, dict):
        errors.append("`by_project` must be a mapping.")
        by_project = {}

    known_ids = set(items.keys())
    referenced_ids: set[str] = set()

    for project_slug, ids in by_project.items():
        if not isinstance(ids, list):
            errors.append(f"`by_project.{project_slug}` must be a list.")
            continue

        seen_in_project: set[str] = set()
        for pub_id in ids:
            if not isinstance(pub_id, str):
                errors.append(f"`by_project.{project_slug}` contains a non-string publication ID.")
                continue
            if pub_id in seen_in_project:
                errors.append(f"`by_project.{project_slug}` contains duplicate ID `{pub_id}`.")
            seen_in_project.add(pub_id)
            referenced_ids.add(pub_id)
            if pub_id not in known_ids:
                errors.append(f"`by_project.{project_slug}` references unknown publication ID `{pub_id}`.")

    orphan_ids = sorted(known_ids - referenced_ids)
    for pub_id in orphan_ids:
        warnings.append(f"`items.{pub_id}` is not referenced by any project.")

    if errors:
        print("Publication data validation failed:\n")
        for msg in errors:
            print(f"- ERROR: {msg}")
        if warnings:
            print("\nWarnings:")
            for msg in warnings:
                print(f"- WARN: {msg}")
        return 1

    print("Publication data validation passed.")
    if warnings:
        print("\nWarnings:")
        for msg in warnings:
            print(f"- WARN: {msg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
