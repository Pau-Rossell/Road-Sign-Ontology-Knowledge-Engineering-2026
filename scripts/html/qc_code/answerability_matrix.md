# CQ Answerability Matrix

Status meanings:
- `yes`: the current ontology/repo has enough structure to answer the CQ directly
- `partial`: a useful answer can be approximated, but some semantics are not modelled explicitly
- `no`: the current ontology/repo does not currently support a defensible answer

| CQ | Status | Main reason |
|---|---|---|
| CQ-01 | yes | Primary sign categories are asserted as subclasses of `RoadSign`. |
| CQ-02 | yes | `PrioritySign` is asserted under `RoadSign`. |
| CQ-03 | yes | Subclasses under `ProhibitoryOrRestrictiveSign` are present. |
| CQ-04 | yes | `B2a_Stop_Octagon` is under `B02_StopSign`, which is under `PrioritySign`. |
| CQ-05 | yes | Mandatory-sign subclasses are present. |
| CQ-06 | yes | Top-level categories are declared disjoint. |
| CQ-07 | yes | The `DangerWarningSign` hierarchy is present. |
| CQ-08 | yes | `B2a_Stop_Octagon` now carries explicit ground, border, and inscription colour axioms. |
| CQ-09 | yes | Circle-sign families now expose explicit border colours that can be queried. |
| CQ-10 | yes | `NormalSizedDangerWarningSign` now carries an explicit `hasStandardSideLength` value. |
| CQ-11 | yes | `B1_GiveWay` has shape `InvertedTriangle`. |
| CQ-12 | partial | Many category/sign classes have shape axioms, but not every class is fully covered. |
| CQ-13 | yes | Many sign classes carry blue-ground restrictions and can be queried directly. |
| CQ-14 | partial | Classes with `hasSpeedValue` can be found, but concrete numeric values are not populated, so the maximum shown cannot be computed. |
| CQ-15 | yes | Pedestrian-related signs now carry explicit applicability axioms via `appliesToCategory` or `appliesExclusivelyToCategory`. |
| CQ-16 | partial | The ontology now links `A11a` and `A11b` to `Falling_rocks`, but the normative “must” choice between models remains convention-dependent. |
| CQ-17 | yes | `A15a` and `A15b` now carry explicit `Domestic_animal` and `Wild_animal` symbol axioms. |
| CQ-18 | yes | Large-vehicle and goods-vehicle restrictions now carry explicit applicability axioms. |
| CQ-19 | yes | Bicycle-only signs now carry explicit exclusivity axioms via `appliesExclusivelyToCategory`. |
| CQ-20 | no | MTSD source files are missing from the current repository snapshot. |
| CQ-21 | no | MTSD source files are missing from the current repository snapshot. |
| CQ-22 | no | MTSD source files are missing from the current repository snapshot. |
| CQ-23 | no | MTSD source files are missing from the current repository snapshot. |
| CQ-24 | no | MTSD source files are missing from the current repository snapshot. |
| CQ-25 | no | MTSD source files are missing from the current repository snapshot. |
