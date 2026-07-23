# Contributing

Two ways to help:

## 1. Submit a hint

Hints live in each lab's `hints.md`. Good hints point someone in the right direction without giving away the answer. No copy-pasteable solutions — if your hint completes a `# TODO` directly, it'll be sent back for revision.

1. [Open a hint issue](https://github.com/open-py-labs/starter-labs/issues/new?template=hint.yml)
2. Fork, add your hint to the relevant `hints.md`, submit a PR linked to the issue

## 2. Submit a new lab

Use [`_lab_template/`](./_lab_template/) as your starting point.

Before opening a PR, make sure that:
- `starter.py` has only `# TODOs`, no solution code
- `test.py` passes on a correct implementation and fails with a readable message (not `AssertionError`)
- The lab teaches a distinct, practical Python skill

1. [Open a lab proposal issue](https://github.com/open-py-labs/starter-labs/issues/new?template=new_lab.yml)
2. Copy `_lab_template/` → `XX-your-lab-name/`, fill out all four files
3. Add your lab to the table in `README.md`, submit a PR

---

Don't be a jerk. This repo is for beginners.
