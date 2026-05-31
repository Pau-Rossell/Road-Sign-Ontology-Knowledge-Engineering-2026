from __future__ import annotations

from _common import (
    ONTOLOGY_PATH,
    label,
    load_graph,
    named_descendants,
    ontology_namespace,
    require_rdflib,
    restriction_fillers,
)


def main() -> None:
    graph = load_graph(ONTOLOGY_PATH)
    ns = ontology_namespace(graph)
    _, _, _, _, OWL, _ = require_rdflib()

    categories = [
        ns.DangerWarningSign,
        ns.PrioritySign,
        ns.ProhibitoryOrRestrictiveSign,
        ns.MandatorySign,
        ns.SpecialRegulationSign,
        ns.InformativeSign,
        ns.AdditionalPanel,
    ]

    for category in categories:
        shapes = set()
        for cls in [category] + named_descendants(graph, category):
            shapes.update(restriction_fillers(graph, cls, ns.hasShape, OWL.hasValue))

        print(f"{label(graph, category)}")
        if shapes:
            for shape in sorted(shapes, key=lambda node: label(graph, node)):
                print(f"  - {label(graph, shape)}")
        else:
            print("  - No explicit shape axioms found in current ontology")
        print()


if __name__ == "__main__":
    main()
