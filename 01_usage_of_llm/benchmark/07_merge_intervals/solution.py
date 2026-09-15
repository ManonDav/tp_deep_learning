def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Trie les intervalles par leur début
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Fusion des intervalles
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)

    return merged