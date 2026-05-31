from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, Iterator


ROOT = Path(__file__).resolve().parents[3]
ONTOLOGY_PATH = ROOT / "ontology" / "roadSignOntology.owl"
ALIGNED_ONTOLOGY_PATH = ROOT / "ontology" / "roadSignOntologyMTSD_aligned.owl"
MTSD_CANDIDATES = [
    ROOT / "data" / "raw" / "MTSD.ttl",
    ROOT / "data" / "raw" / "mtsd.ttl",
    ROOT / "data" / "raw" / "MTSD.owl",
    ROOT / "data" / "processed" / "MTSD.ttl",
]


def require_rdflib():
    try:
        from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise SystemExit(
            "This script requires rdflib. Install it in the project environment first."
        ) from exc
    return Graph, Namespace, RDF, RDFS, OWL, URIRef


def load_graph(path: Path):
    Graph, _, _, _, _, _ = require_rdflib()
    graph = Graph()
    graph.parse(path)
    return graph


def ontology_namespace(graph):
    _, Namespace, _, _, _, _ = require_rdflib()
    for prefix, namespace in graph.namespaces():
        if prefix == "":
            return Namespace(str(namespace))
    return Namespace("http://www.semanticweb.org/ontologies/2026/4//")


def label(graph, node) -> str:
    _, _, _, RDFS, _, _ = require_rdflib()
    value = graph.value(node, RDFS.label)
    if value is not None:
        return str(value)
    iri = str(node)
    return iri.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def named_class_local_name(node) -> str:
    return str(node).rsplit("#", 1)[-1]


def named_descendants(graph, root) -> list:
    _, _, _, RDFS, OWL, _ = require_rdflib()
    seen = set()
    queue = [root]
    descendants = []
    while queue:
        parent = queue.pop(0)
        for child in graph.subjects(RDFS.subClassOf, parent):
            if child in seen:
                continue
            if (child, None, OWL.Restriction) in graph:
                continue
            seen.add(child)
            descendants.append(child)
            queue.append(child)
    return descendants


def superclass_closure(graph, cls) -> set:
    _, _, _, RDFS, OWL, _ = require_rdflib()
    seen = {cls}
    queue = [cls]
    while queue:
        current = queue.pop(0)
        for parent in graph.objects(current, RDFS.subClassOf):
            if parent in seen:
                continue
            if (parent, None, OWL.Restriction) in graph:
                continue
            seen.add(parent)
            queue.append(parent)
    return seen


def restriction_fillers(graph, cls, prop, filler_predicate) -> set:
    _, _, RDF, RDFS, OWL, _ = require_rdflib()
    fillers = set()
    for candidate in superclass_closure(graph, cls):
        for parent in graph.objects(candidate, RDFS.subClassOf):
            if (parent, RDF.type, OWL.Restriction) not in graph:
                continue
            if (parent, OWL.onProperty, prop) not in graph:
                continue
            for filler in graph.objects(parent, filler_predicate):
                fillers.add(filler)
    return fillers


def classes_with_data_property_restriction(graph, prop) -> list:
    _, _, RDF, RDFS, OWL, _ = require_rdflib()
    classes = set()
    for cls, _, parent in graph.triples((None, RDFS.subClassOf, None)):
        if (parent, RDF.type, OWL.Restriction) in graph and (parent, OWL.onProperty, prop) in graph:
            classes.add(cls)
    return sorted(classes, key=lambda node: label(graph, node))


def find_mtsd_source() -> Path | None:
    for candidate in MTSD_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def fail_if_mtsd_missing() -> Path:
    mtsd = find_mtsd_source()
    if mtsd is None:
        raise SystemExit(
            "MTSD source file not found. Expected one of:\n- "
            + "\n- ".join(str(path) for path in MTSD_CANDIDATES)
        )
    return mtsd
