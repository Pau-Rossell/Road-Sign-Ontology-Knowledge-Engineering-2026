import json, os
from alignment_module import alignment

occluded_signs = set()
for filename in os.listdir("mtsd_dataset/annotations"):
    with open(os.path.join("mtsd_dataset/annotations", filename), 'r') as f:
        data = json.load(f)
        for obj in data.get("objects", []):
            if obj.get("properties", {}).get("occluded", False):
                label = obj.get("label")
                aligned_classes = alignment.label_to_road_classes.get(label, "Not Aligned")
                occluded_signs.add((label, str(aligned_classes)))

for label, classes in occluded_signs:
    print(f"MTSD Label: {label} --> Aligned to: {classes}")