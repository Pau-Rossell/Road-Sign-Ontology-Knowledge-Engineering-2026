import json

with open("mtsd_dataset/annotations/–7fWq6WjZM8L1eUSuvOEA.json", 'r') as f:
    image_data = json.load(f)

sign_count = len(image_data.get("objects", []))
print(f"Total road signs depicted: {sign_count}")