from owlready2 import *

onto_path.append(".")
onto = get_ontology("roadSignOntology.owl").load()

with onto:
    sync_reasoner_pellet(infer_data_property_values=True)

speed_signs = []
max_speed = 0

# Iterate through all road sign classes
for cls in onto.RoadSign.descendants():
    has_speed = False
    for prop in cls.get_class_properties():
        # Checking for data properties related to speed values (e.g., hasSpeedValue)
        if prop.name in ["hasSpeedValue", "hasValue", "speedLimit"]:
            has_speed = True
            break
            
    if has_speed:
        speed_signs.append(cls.name)
        # Attempt to retrieve the value if it's explicitly modeled as a data restriction
        for restriction in cls.is_a:
            if isinstance(restriction, Restriction) and restriction.property.name in ["hasSpeedValue", "hasValue", "speedLimit"]:
                if isinstance(restriction.value, int) and restriction.value > max_speed:
                    max_speed = restriction.value

print("Signs carrying a speed value:")
for sign in set(speed_signs):
    print(f"- {sign}")

print(f"\nThe maximum speed explicitly modeled is: {max_speed} km/h")