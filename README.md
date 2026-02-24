# jgarciab.github.io

Minimal Jekyll website for GitHub Pages.

## Pages
- About
- Research
- Teaching
- CV
- Team

## Data Files
- `_data/research.yml`: research tiles (homepage summary, colors, years, status).
- `_data/research_projects.yml`: project narratives and grants.
- `_data/publications.yml`: publication metadata and per-project publication mapping.
  - `items`: one canonical record per publication.
  - `by_project`: ordered publication IDs shown on each project page.
- `_data/teaching_main.yml`, `_data/teaching_other.yml`: teaching tiles and additional courses/workshops.
- `_data/people.yml`, `_data/other_master_students.yml`: team and supervision entries.
- `_data/cv.yml`: CV sections.

## Local build
```bash
bundle install
bundle exec jekyll serve
```

## Editing Notes
- Keep publication metadata only in `_data/publications.yml`.
- To change the publication order on a project page, edit `by_project.<project-slug>`.
- Project pages render through `_includes/research_project_content.html`.

## Data Validation
```bash
python3 scripts/validate_publications.py
```
