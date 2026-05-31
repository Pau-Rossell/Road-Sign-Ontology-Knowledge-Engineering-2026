from __future__ import annotations

from _common import ONTOLOGY_PATH, classes_with_data_property_restriction, label, load_graph, ontology_namespace


def main() -> None:
    graph = load_graph(ONTOLOGY_PATH)
    ns = ontology_namespace(graph)
    classes = classes_with_data_property_restriction(graph, ns.hasSpeedValue)

    print("Signs carrying a speed value restriction:")
    if not classes:
        print("- None found")
    else:
        for cls in classes:
            print(f"- {label(graph, cls)}")

    print()
    print("Maximum speed shown on most speed limit signs:")
    print(
        "Not computable from the current ontology, because it models the existence "
        "of a speed value but does not populate concrete numeric literals for sign classes."
    )


if __name__ == "__main__":
    main()
