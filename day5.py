def overlap_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the starting point
    intervals.sort(key=lambda x: x[0])
    
    overlapping_intervals = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        # Check if the current interval overlaps with the previous one
        if start <= current_end: 
            # If overlap,update the end of the current interval to the maximum end
            current_end = max(current_end, end)
        else:
            # If no overlap, add the previous interval to the result
            overlapping_intervals.append([current_start, current_end])
            current_start, current_end = start, end

    # Add the last interval
    overlapping_intervals.append([current_start, current_end])

    return overlapping_intervals

# Example:
input_intervals = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]
result = overlap_intervals(input_intervals)
print(result)