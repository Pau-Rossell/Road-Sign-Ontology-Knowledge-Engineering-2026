import json, os
from alignment_module import alignment, onto 

images_with_target = []
for filename in os.listdir("mtsd_dataset/annotations"):
    with open(os.path.join("mtsd_dataset/annotations", filename), 'r') as f:
        data = json.load(f)
        
    for obj in data.get("objects", []):
        if alignment.label_is_aligned_to(obj.get("label"), onto.CompulsoryMinimumSpeed):
            images_with_target.append(filename)
            break

print("Images containing CompulsoryMinimumSpeed:", images_with_target)