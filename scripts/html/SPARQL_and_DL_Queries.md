# Competency Questions: SPARQL and DL Queries

## Category A — Taxonomy
Structure and classification of road signs.

### CQ-01
**Question:** What are the primary kinds of road signs distinguished in the Vienna Convention?  
**Method:** SPARQL
```sparql
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rs: [http://example.org/roadsigns#](http://example.org/roadsigns#)

SELECT ?primaryKind
WHERE {
    ?primaryKind rdfs:subClassOf rs:RoadSign .
}
```

### CQ-02
Question: Is a priority sign considered a type of road sign?

Method: DL query

PrioritySign

### CQ-03
Question: What are the subclasses of ProhibitoryOrRestrictiveSign defined in the Vienna Convention?

Method: SPARQL
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rs: [http://example.org/roadsigns#](http://example.org/roadsigns#)

SELECT ?subclass
WHERE {
    ?subclass rdfs:subClassOf rs:ProhibitoryOrRestrictiveSign .
}


### CQ-04
Question: Is a STOP sign (B2) a type of priority sign?

Method: DL query

B2_Stop

### CQ-05
Question: What types of signs belong to the mandatory signs category?

Method: SPARQL
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rs: [http://example.org/roadsigns#](http://example.org/roadsigns#)

SELECT ?subclass
WHERE {
    ?subclass rdfs:subClassOf rs:MandatorySign .
}

### CQ-06
Question: Are danger warning signs and mandatory signs disjoint categories?

Method: DL query

DangerWarningSign and MandatorySign

### CQ-07
Question: What is the complete class hierarchy under DangerWarningSign?

Method: SPARQL
PREFIX rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
PREFIX rs: [http://example.org/roadsigns#](http://example.org/roadsigns#)

SELECT ?subclass
WHERE {
    ?subclass rdfs:subClassOf* rs:DangerWarningSign .
}

Category B — Properties
Physical and visual attributes of road signs.

### CQ-08
Question: What are the required background and border colours for a model B2a STOP sign?

Method: DL query

Plaintext
B2a_Stop

### CQ-09
Question: Which border colours can circle-shaped road signs have?

Method: DL query

Plaintext
Colour and inverse (hasBorderColour) some (RoadSign and hasShape value Circle)

### CQ-10
Question: What is the standard measurement for the side of a normal-sized danger warning sign?

Method: SPARQL
PREFIX rs: [http://example.org/roadsigns#](http://example.org/roadsigns#)

SELECT ?measurement
WHERE {
    rs:DangerWarningSign rs:hasSideMeasurement ?measurement .
}

### CQ-11
Question: What shape does a give-way sign (B1) have?

Method: DL query

Shape and inverse (hasShape) some B1_GiveWay

### CQ-13
Question: Which road signs have a blue ground colour?

Method: DL query

RoadSign and hasGroundColour value Blue

