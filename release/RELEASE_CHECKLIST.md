# Release Checklist

Use this checklist before tagging a public course release.

## Content

- [ ] README links point to the current course structure
- [ ] `COURSE.md` and `COURSE_zh.md` list current modules
- [ ] `DIRECTORY.md` indexes new folders and templates
- [ ] New curriculum chapters have English and Traditional Chinese versions
- [ ] New examples have `README.md` and `README_zh.md`
- [ ] Launch kit reflects the current value proposition

## Verification

- [ ] `python scripts/verify_examples.py` passes locally
- [ ] `python benchmarks/benchmark_runner.py` passes locally
- [ ] GitHub Actions verify workflow passes
- [ ] GitHub Pages deploy workflow passes
- [ ] Website returns HTTP 200

## Project Hygiene

- [ ] `CHANGELOG.md` is updated
- [ ] No runtime artifacts are committed
- [ ] No `__pycache__` folders are committed
- [ ] No secrets, API keys, tokens, or private notes are committed
- [ ] Issue templates and PR template match the current contribution workflow

## Release Notes

```text
Title:
Date:
Tag:

Highlights:
- 

New examples:
- 

New curriculum:
- 

Verification:
- 
```

