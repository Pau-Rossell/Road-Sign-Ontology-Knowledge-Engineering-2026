# Protégé Desktop tutorial for the road-sign ontology project

## Executive summary

This tutorial is designed for building `project/ontology/roadSignOntology.owl` in Protégé Desktop, not WebProtégé. Protégé Desktop is the standalone OWL 2 editor with direct support for reasoners such as HermiT, and the official documentation used here explicitly targets Protégé versions 4, 5, and newer. For your project, the practical session loop is: create the ontology in RDF/XML, build the Vienna Convention class scaffold, add a small controlled vocabulary for shapes and colours, add the project’s key object and data properties, define a few sign classes in Manchester Syntax, classify with HermiT, inspect the inferred hierarchy and any red classes under `owl:Nothing`, save screenshots to `project/results/screenshots/`, and append a session note to `project/docs/prompt_log.md`. citeturn0search3turn2view2turn24view0turn9view0turn9view2turn10view1

A strong project pattern is to separate two modelling layers from the start: sign types as classes, and MTSD sign observations as individuals that carry bounding-box and occlusion data. That is a practical inference from OWL’s distinction between classes, individuals, object properties, and datatype properties, and it fits Protégé’s class, individual, object-property, and data-property views cleanly. citeturn7search0turn10view3turn25view0

## Set up Protégé and your project files

The setup steps below follow Protégé’s official startup, menu, navigation, preferences, and rendering documentation. citeturn9view0turn24view0turn4view3turn13search2

- Open Protégé and choose `File > New...`, or use the welcome screen option for creating a new OWL ontology.
- Use an ontology IRI such as `http://example.org/roadSignOntology` if you do not yet have a permanent public IRI.
- Set the physical save location to `project/ontology/roadSignOntology.owl`.
- Choose `RDF/XML` as the ontology format.
- If you want a single main workspace, stay in the `Entities` tab. Protégé’s guide calls this the “workhorse” tab because it lets you browse classes, properties, and individuals from one place. If you prefer dedicated panes, enable `Window > Tabs > Classes`, `Object Properties`, `Data Properties`, and `Individuals`. citeturn24view0turn25view0
- If your entity names later become hard to read, open `File > Preferences > Renderer` and choose rendering by annotation values or URI fragment, depending on whether you will use labels such as `rdfs:label`. Protégé also lets you configure how new entity URIs and labels are generated under `File > Preferences > New Entities`. citeturn4view3turn13search2turn24view0

Two helpful official screenshot links for orientation are below.

- Protégé asserted class hierarchy screenshot: [https://protegewiki.stanford.edu/images/7/7f/Assertedclasshierarchy.png](https://protegewiki.stanford.edu/images/7/7f/Assertedclasshierarchy.png)
- Protégé class description screenshot: [https://protegewiki.stanford.edu/images/thumb/2/2f/Classdescription.png/400px-Classdescription.png](https://protegewiki.stanford.edu/images/thumb/2/2f/Classdescription.png/400px-Classdescription.png)

## Build the starter ontology

Annex 1 of the Vienna Convention organizes road signs into sections such as danger warning, priority, prohibitory or restrictive, mandatory, special regulation, information/facilities/service, direction/position/indication, and additional panels. A clean starter hierarchy in Protégé can mirror those sections, while also adding a few project helper classes such as `Shape`, `Colour`, and `DetectedSignObject`. citeturn28search17turn15search15turn28search12turn28search14

- In the class hierarchy, select `owl:Thing`.
- Use the `Add Subclass` icon in the class hierarchy, or `Edit > Create child`, to add `RoadSign`.
- Under `RoadSign`, create these starter subclasses:

```text
RoadSign
    DangerWarningSign
    PrioritySign
    ProhibitoryOrRestrictiveSign
    MandatorySign
    SpecialRegulationSign
    InformationFacilityServiceSign
    DirectionPositionIndicationSign
    AdditionalPanel
Shape
Colour
DetectedSignObject
```

- If you want to build that hierarchy faster, Protégé’s `Tools > Create class hierarchy...` lets you paste a tab-indented class list. citeturn27search7turn27search4

Next, add the controlled vocabulary individuals for shapes and colours. Protégé’s individual views and tabs can be enabled from the `Window` menu, and the `Property assertions` view is the right place for entering facts about individuals. citeturn25view0

- Open the `Individuals` tab, or add `Window > Views > Individual views > Individuals by type` and `Property assertions` if those views are hidden.
- Create individuals under `Colour` such as `Red`, `White`, `Blue`, and `Yellow`.
- Create individuals under `Shape` such as `Circle`, `Triangle`, and `Octagon`.
- If you want your small controlled vocabularies to be explicitly distinct, Protégé’s `Edit > Make all individuals distinct...` can generate an `allDifferent` axiom. citeturn27search0

Now add the main properties. Protégé’s object-property description view contains `Domains` and `Ranges`, and its data-property description view is similar except the range is a datatype. A very important novice pitfall is that multiple entered domains or ranges are treated as an intersection, not an “either/or.” citeturn10view3

A solid property plan for this project is:

```text
Object properties
- hasShape
  Domain: RoadSign
  Range: Shape

- hasGroundColour
  Domain: RoadSign
  Range: Colour

- hasBorderColour
  Domain: RoadSign
  Range: Colour

Data properties
- hasTextValue
  Domain: RoadSign
  Range: xsd:string

- hasSpeedValue
  Domain: RoadSign
  Range: xsd:integer

- xmin
  Domain: DetectedSignObject
  Range: xsd:integer

- ymin
  Domain: DetectedSignObject
  Range: xsd:integer

- xmax
  Domain: DetectedSignObject
  Range: xsd:integer

- ymax
  Domain: DetectedSignObject
  Range: xsd:integer

- isOccluded
  Domain: DetectedSignObject
  Range: xsd:boolean
```

That datatype choice matches OWL’s built-in XML Schema datatype support and Protégé’s data-property editor. `xsd:integer` and `xsd:boolean` are the simplest starting points for this project; if you later normalize coordinates to fractional values, switch the bounding-box properties to `xsd:decimal`. citeturn26search10turn10view3

A practical MTSD-style example individual can look like this:

```text
Individual: mtsd_sign_000001
  Types: DetectedSignObject, StopSign
  Facts:
    hasShape Octagon
    hasGroundColour Red
  DataPropertyAssertions:
    xmin 142
    ymin 88
    xmax 231
    ymax 181
    isOccluded false
```

This is a project-oriented pattern: the bounding box and occlusion belong to the observed sign object, not to the sign class definition itself. citeturn7search0turn25view0

## Define sign classes in Manchester Syntax

Protégé uses Manchester OWL Syntax in its expression editor, and the W3C Manchester grammar distinguishes carefully between `some`, `only`, and `value`. In particular, if `Octagon` and `Red` are individuals, you must use `value Octagon` and `value Red`; `some` expects a class expression instead. For data properties, `value` takes a literal such as `120` or `"STOP"`. Protégé’s expression editor also supports autocomplete with `Ctrl+Space`. citeturn4view0turn23search0turn23search6

The distinction below is the one that matters most when building sign definitions.

| meaning | when to use |
|---|---|
| `rdfs:subClassOf` means every instance of class A is also an instance of class B | Use it for one-way taxonomy statements such as `StopSign subClassOf PrioritySign` or `MaximumSpeedLimit120 subClassOf ProhibitoryOrRestrictiveSign` |
| `owl:equivalentClass` means class A and the target expression have exactly the same members | Use it when you are giving a necessary-and-sufficient definition that should drive automated classification |

This is exactly how OWL equivalence works semantically, and it is also the distinction behind Protégé’s “primitive” versus “defined” class workflow and the `Edit > Convert to defined class` command. citeturn0search7turn27search0turn10view1

For this project, two copy-paste-ready example definitions are below.

```text
Class: StopSign
  SubClassOf:
    PrioritySign
  EquivalentTo:
    PrioritySign
    and hasShape value Octagon
    and hasGroundColour value Red
    and hasTextValue value "STOP"
```

```text
Class: MaximumSpeedLimit120
  SubClassOf:
    ProhibitoryOrRestrictiveSign
  EquivalentTo:
    ProhibitoryOrRestrictiveSign
    and hasShape value Circle
    and hasGroundColour value White
    and hasBorderColour value Red
    and hasSpeedValue value 120
```

These are tutorial examples, not the only defensible models. The Vienna sources support the relevant sign families and visual traits: the STOP sign is a priority sign and the European Agreement’s B2a model is octagonal with red ground and white “STOP”; the GIVE WAY sign is an inverted triangle with a white or yellow ground and red border; and prohibitory or restrictive signs are circular, normally with white or yellow ground and a wide red border. The Vienna speed-limit sign C-14.1 expresses the permitted maximum speed, so `MaximumSpeedLimit120` is best understood as a project-specific value-specialized subclass of the Vienna speed-limit family rather than as a universal top-level Vienna class. citeturn16search24turn17search24turn19search1turn18search14

To enter those definitions in Protégé:

- Select the class in the class hierarchy.
- In the `Description` view, click the `+` next to `Equivalent classes`.
- Choose the class expression editor.
- Paste the Manchester expression.
- If you prefer, add superclass restrictions one by one first and then use `Edit > Convert to defined class` or `Ctrl+D`. Protégé’s documentation explicitly says that converting to a defined class builds an intersection from the current superclasses. citeturn10view1turn4view0turn27search0turn27search6

## Classify and debug with HermiT

Protégé’s official documentation describes HermiT as the built-in reasoner workflow for classifying the ontology. Depending on the exact desktop build, you may select `Reasoner > HermiT` and then `Reasoner > Start Reasoner`, or the selection may immediately initialize classification. After classification, the inferred class hierarchy appears, and unsatisfiable classes are shown in red under `owl:Nothing`. The `DL Query` tab only works on a classified ontology. citeturn24view0turn9view2turn4view2turn10view1

A clean reasoning loop for this project is:

- Save the ontology.
- Open `Reasoner > HermiT`.
- Run `Reasoner > Start Reasoner`.
- After edits, use `Reasoner > Synchronize Reasoner`.
- Inspect `Entities > Class hierarchy (inferred)`.
- If needed, enable `Window > Tabs > DL Query` and test expressions such as `PrioritySign and hasShape value Octagon` or `ProhibitoryOrRestrictiveSign and hasSpeedValue value 120`. citeturn9view2turn4view2turn25view0

The most common modelling mistakes in this kind of ontology are:

- Using `EquivalentTo` when you only intended a one-way `SubClassOf` statement. That can over-constrain the class and create bad inferences. citeturn0search7turn27search0
- Using `some Octagon` even though `Octagon` is an individual. In this tutorial pattern, the correct syntax is `hasShape value Octagon`. citeturn23search0turn4view0
- Entering several domains or ranges while thinking they mean alternatives. In Protégé they are treated as an intersection. citeturn10view3
- Expecting OWL to behave like a closed database. In OWL, missing information is not false information; that is the open-world assumption. citeturn8search0
- Adding strong disjointness too early. Disjointness is useful, but it can easily make classes unsatisfiable, which Protégé then shows under `owl:Nothing`. citeturn7search0turn10view1
- Using string literals where proper datatypes are better, such as `"true"` instead of the boolean literal `true`, or `"120"` instead of the integer literal `120`. citeturn26search10turn10view3
- Putting `xmin`, `ymin`, `xmax`, `ymax`, or `isOccluded` into class definitions. Those belong on observation individuals such as MTSD sign objects, not on taxonomy classes like `StopSign`. citeturn7search0turn25view0

If a class turns red under `owl:Nothing`, inspect the class’s `Equivalent classes`, `Disjoint classes`, and any recently changed property domains/ranges first. A very pragmatic debugging tactic is to temporarily replace an `EquivalentTo` definition with `SubClassOf` axioms, re-run HermiT, and see whether the contradiction disappears. Protégé’s views make those exact locations visible in the class description and inferred hierarchy. citeturn10view1turn10view2turn10view3

Protégé also supports closure axioms from the class description view context menu. That matters because, under open-world semantics, saying what a sign has does not automatically say that it has only those values. If you later need closed descriptions such as “only these fillers on this property,” the closure-axiom tool is a useful next step. citeturn10view2turn8search0

## Save outputs and log each session

Protégé’s file menu supports `Save` and `Save As`, and the startup workflow lets you choose RDF/XML as the physical serialization. The window menu also exposes an `RDF/XML rendering` ontology view, so you can inspect the serialization inside the UI before or after saving. citeturn9view0turn9view3turn25view0

Use this output routine for the project:

- Save the ontology to `project/ontology/roadSignOntology.owl`.
- Keep screenshots in `project/results/screenshots/`.
- At minimum, capture:
  - the asserted hierarchy,
  - the inferred hierarchy after HermiT,
  - any unsatisfiable classes under `owl:Nothing`,
  - one sample class description showing an equivalent class definition,
  - one screenshot of RDF/XML rendering or the saved ontology visible in Protégé.
- Use readable filenames such as:
  - `project/results/screenshots/2026-05-31_asserted_hierarchy.png`
  - `project/results/screenshots/2026-05-31_inferred_hierarchy.png`
  - `project/results/screenshots/2026-05-31_unsat_classes.png`
  - `project/results/screenshots/2026-05-31_stopsign_definition.png`
  - `project/results/screenshots/2026-05-31_rdfxml_rendering.png`

For `project/docs/prompt_log.md`, keep one entry per Protégé session, and if the session came from an LLM instruction, paste that exact initiating prompt into `USER_PROMPT`. If the session was fully manual and your project rules allow it, use a neutral manual session label. A short checklist for each entry is:

- what ontology file you modified,
- what classes or properties you created or changed,
- what Manchester definitions you added,
- whether HermiT ran successfully,
- whether expected inferred subclasses appeared,
- whether any classes became unsatisfiable,
- what screenshots you saved,
- what unresolved modelling questions remain.

Use this strict entry template:

```text
### PROMPT LOG ENTRY START
- ENTRY_ID: 2026-05-31-protege-session-01
- TIMESTAMP: 2026-05-31T18:40:00+02:00
- USER_PROMPT: |
  Manual Protégé session for roadSignOntology.owl
- SUMMARY_OF_ACTIONS: |
  Created core Vienna sign classes under RoadSign.
  Added object and data properties for shape, colour, speed, bounding boxes, and occlusion.
  Added Manchester definitions for StopSign and MaximumSpeedLimit120.
  Ran HermiT and inspected the inferred hierarchy.
- FILES_CREATED:
  - project/results/screenshots/2026-05-31_inferred_hierarchy.png
  - project/results/screenshots/2026-05-31_stopsign_definition.png
- FILES_MODIFIED:
  - project/ontology/roadSignOntology.owl
  - project/docs/prompt_log.md
- FILES_DELETED:
  - None
- COMMANDS_RUN: |
  None
- KEY_DECISIONS: |
  Kept detected sign objects separate from sign taxonomy classes.
  Used controlled vocabulary individuals for Colour and Shape.
  Used xsd:integer for speed and pixel coordinates.
- OPEN_ISSUES: |
  Decide whether to model model-specific STOP variants separately.
  Decide whether border colour should be mandatory for all restrictive signs.
### PROMPT LOG ENTRY END
```

## Official resources and image links

These are the most relevant official references for the workflow above. Protégé’s software page, user documentation home, quick-start guide, views guide, expression editor guide, DL Query guide, and the W3C OWL references are the core sources; the Vienna Convention resource page is the authoritative legal reference if you need to justify sign categories or physical conventions. citeturn0search3turn2view2turn24view0turn3view0turn4view0turn4view2turn7search0turn23search6turn0search1

- Protégé Desktop software and download: [https://protege.stanford.edu/software/](https://protege.stanford.edu/software/)
- Protégé Desktop user documentation home: [https://protegewiki.stanford.edu/wiki/ProtegeDesktopUserDocs](https://protegewiki.stanford.edu/wiki/ProtegeDesktopUserDocs)
- Getting started with Protégé Desktop: [https://protegewiki.stanford.edu/wiki/Protege4GettingStarted](https://protegewiki.stanford.edu/wiki/Protege4GettingStarted)
- Protégé views guide: [https://protegewiki.stanford.edu/wiki/Protege4Views](https://protegewiki.stanford.edu/wiki/Protege4Views)
- Protégé expression editor: [https://protegewiki.stanford.edu/wiki/Protege4ExpressionEditor](https://protegewiki.stanford.edu/wiki/Protege4ExpressionEditor)
- Protégé DL Query tab: [https://protegewiki.stanford.edu/wiki/DLQueryTab](https://protegewiki.stanford.edu/wiki/DLQueryTab)
- W3C OWL 2 Primer: [https://www.w3.org/TR/owl2-primer/](https://www.w3.org/TR/owl2-primer/)
- W3C OWL 2 Manchester Syntax: [https://www.w3.org/TR/owl2-manchester-syntax/](https://www.w3.org/TR/owl2-manchester-syntax/)
- UNECE Vienna Convention resource page: [https://unece.org/info/publications/pub/2637](https://unece.org/info/publications/pub/2637)

A useful supplementary beginner-oriented walkthrough is the Protégé Pizza tutorial PDF you uploaded. fileciteturn0file0