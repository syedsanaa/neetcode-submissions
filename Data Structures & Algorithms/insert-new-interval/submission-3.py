class Solution:
    def insert(self, intervals, newInterval):
        res = []
        s, e = newInterval
        i, n = 0, len(intervals)

        while i < n and intervals[i][1] < s:      # strictly before
            res.append(intervals[i]); i += 1

        while i < n and intervals[i][0] <= e:     # overlapping (touching counts)
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        res.append([s, e])

        res.extend(intervals[i:])                 # strictly after
        return res
            