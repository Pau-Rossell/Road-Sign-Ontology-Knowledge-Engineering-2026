from alignment_module import mtsd, alignment, onto

prohibitory_count = sum(
    count for label, count in mtsd.label_counts.items()
    if alignment.label_is_aligned_to(label, onto.ProhibitoryOrRestrictiveSign)
)

print(f"Percentage against all objects: {prohibitory_count / mtsd.total_objects * 100:.2f}%")