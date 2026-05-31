from alignment_module import mtsd, alignment, onto

categories = [onto.DangerWarningSign, onto.PrioritySign, onto.ProhibitoryOrRestrictiveSign, onto.MandatorySign]
distribution = {cat.name: 0 for cat in categories}

for label, count in mtsd.label_counts.items():
    for cat in categories:
        if alignment.label_is_aligned_to(label, cat):
            distribution[cat.name] += count
            break 

for category_name, count in distribution.items():
    print(f"{category_name}: {count}")