from alignment_module import mtsd, alignment, onto

found = any(alignment.label_is_aligned_to(label, onto.RestrictionForHeavyVehicles) 
            for label in mtsd.label_counts.keys())

print("Road signs applicable to lorries found in dataset?" , "Yes" if found else "No")