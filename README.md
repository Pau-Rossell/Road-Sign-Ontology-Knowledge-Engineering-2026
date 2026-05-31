### KNOWLEDGE ENGINEERING: ROAD SIGN ONTOLOGY PROJECT README
This file contains the basic information on the project architecture:

```
project/
├── ontology/                           / This holds the actual .owl ontologies
│   ├── roadSignOntology.owl            / The class taxonomy
│   └── roadSignOntologyMTSD_aligned    / The actual MTSD aligned ontology
│
├── data/
│   ├── raw
│   │   └── MTSD.ttl                    / Mappillary Trafic Sign Dataset
│   └── processed
│       └── mtsd_alignment_mapping      / CSV to align roadSignOntology and MTSD.ttl
│
├── queries/                            / Contains the python, SPARQL,... queries for each CQ
│
├── scripts/                            / Contains .html auxiliary files that aided us in comprehending the project composition
│
├── docs/
│   ├── KnowledgeEngineeringSessions/   / KE sessions PDFs
│   ├── competency_questions.md         / The CQs
│   ├── prompt_log.md                  / Structured LLM prompts log
│   ├── Conv_road_signs_2006v_EN.pdf    / The Vienna Convention on road signs as shared in the Virtual Campus
│   └── ontologyFormat                  / Specifies the format to be used throughout our ontology
│
├── AGENTS.md                           / Prompt which serves as contex for any agent working within the directory.
└── README.md                           / INFO on the project directory architecture
```