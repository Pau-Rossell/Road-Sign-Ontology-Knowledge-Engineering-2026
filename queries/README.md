# CQ Query Pack

This folder contains one artifact per competency question in `docs/competency_questions.md`.

Conventions:
- `cqNN_*.rq`: SPARQL queries for ontology inspection
- `cqNN_*.dl.txt`: Protégé DL Query expressions and notes
- `cqNN_*.py`: Python scripts for questions that were planned as procedural queries
- `_common.py`: shared helper utilities for the Python scripts
- `answerability_matrix.md`: what the current ontology/repo can answer now

Notes:
- The ontology-focused files target `ontology/roadSignOntology.owl`.
- The MTSD-focused scripts currently detect and report that the dataset source is missing from this repository snapshot.
- DL query files are meant to be pasted into Protégé's DL Query tab.
