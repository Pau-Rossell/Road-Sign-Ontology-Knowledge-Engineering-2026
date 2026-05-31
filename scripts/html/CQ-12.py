from owlready2 import *

# Load the ontology
onto_path.append("./ontology")
onto = get_ontology("roadSignOntology.owl").load()

with onto:
    sync_reasoner_pellet(infer_property_values=True)

def get_shapes_for_category(category_cls):
    shapes = set()
    for cls in category_cls.descendants(include_self=True):
        for restriction in cls.is_a:
            # Look for Restrictions on the hasShape property
            if isinstance(restriction, Restriction) and restriction.property == onto.hasShape:
                value = restriction.value
                if value is not None:
                    shapes.add(value)
    return shapes

# Traffic sign categories (rooted at RoadSign)
categories = [
    onto.DangerWarningSign,
    onto.PrioritySign,
    onto.ProhibitoryOrRestrictiveSign,
    onto.MandatorySign,
    onto.SpecialRegulationSign,
    onto.InformationFacilityServiceSign,
    onto.DirectionPositionIndicationSign,
    onto.AdditionalPanel
]

print("Shapes associated with each traffic sign category:\n")
for category in categories:
    shapes = get_shapes_for_category(category)
    print(f"- {category.name}:")
    if shapes:
        for shape in sorted(shapes, key=lambda s: s.name):
            print(f"   {shape.name}")
    else:
        print("   (no shape entailed)")