Ontology file format:
RDF/XML
File: ontology/roadSignOntology.owl

Ontology IRI:
https://github.com/Pau-Rossell/Road-Sign-Ontology-Knowledge-Engineering-2026/RoadSignOntology

Entity IRI pattern:
https://github.com/Pau-Rossell/Road-Sign-Ontology-Knowledge-Engineering-2026/RoadSignOntology#EntityName


--------------------------------------------


Classes:
Use PascalCase.
Examples:
RoadSign
PrioritySign
DangerWarningSign
MaximumSpeedLimitSign
B2_Stop
C14_MaximumSpeedLimit


--------------------------------------------


Individuals:
Use PascalCase.
Examples:
Red
DarkBlue
Circle
Octagon
Pedestrian
MotorVehicle

Pattern:
Red rdf:type Colour
Circle rdf:type Shape
Pedestrian rdf:type RoadUserCategory


--------------------------------------------


Object properties:
Use camelCase.
Examples:
hasShape
hasGroundColour
hasBorderColour
hasSymbol
appliesToUserCategory
appliesToVehicleCategory

Use when linking an entity to another entity or controlled vocabulary individual.
Example:
B2_Stop SubClassOf hasShape value Octagon


--------------------------------------------


Data properties:
Use camelCase.
Examples:
hasSpeedValue
hasTextValue
imageWidth
imageHeight
xmin
ymin
xmax
ymax
isOccluded

Use when linking an entity to a literal value.
Examples:
hasSpeedValue 50
hasTextValue "STOP"
isOccluded true


--------------------------------------------


Subclass relations:
Use rdfs:subClassOf for IS-A relations.
Example:
PrioritySign rdfs:subClassOf RoadSign
B2_Stop rdfs:subClassOf PrioritySign


--------------------------------------------


Equivalence:
Use owl:equivalentClass only for exact class equivalence or full necessary-and-sufficient definitions.
Example:
B2_Stop EquivalentTo PrioritySign and hasShape value Octagon and hasGroundColour value Red


--------------------------------------------


MTSD labels:
Preserve original label text using rdfs:label.
Use subclasses for narrower MTSD labels.
Example:
regulatory--maximum-speed-limit-120 rdfs:subClassOf MaximumSpeedLimitSign


--------------------------------------------


Datatypes:
xsd:string for text
xsd:boolean for true/false
xsd:integer for whole numbers
xsd:decimal for coordinates/measurements
xsd:anyURI for URI-like values


--------------------------------------------


Annotations:
Use rdfs:label for human-readable names.
Use rdfs:comment for explanations or source notes.
Use dc:source or similar annotation only if already included/imported or clearly declared.


--------------------------------------------


Disjointness:
Use cautiously.
Classes: use owl:disjointWith only where categories cannot overlap.
Individuals: use DifferentFrom or AllDifferent, not disjointWith.


--------------------------------------------


Relationships summary:
Class to class: rdfs:subClassOf
Individual to class: rdf:type
Class to individual value: object property + value restriction
Entity to literal: data property