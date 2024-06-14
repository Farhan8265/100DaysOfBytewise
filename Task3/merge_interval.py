# Exercise: Merge Intervals
def merge_interval(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            merged.append(interval)
    return merged

input_interval = []
while True:
    interval_str = input("Enter an interval (start,end) or 'done' to finish: ")
    if interval_str.lower() == 'done':
        break
    interval = tuple(map(int, interval_str.split(',')))
    input_interval.append(interval)

merge_interval = merge_interval(input_interval)

print("Merged Intervals:", merge_interval)
